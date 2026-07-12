import struct
import zlib


# 用于获取 index-1 表偏移量的移位位数
SHIFT_1 = 6 + 5 

# 用于获取 index-2 表偏移量的移位位数
SHIFT_2 = 5 

# 两个移位位数的差值，用于从 index-2 偏移量计算 index-1 偏移量（6=11-5）
SHIFT_1_2 = SHIFT_1 - SHIFT_2 

# BMP（基本多文种平面）的 index-1 条目数（32=0x20）
# 这部分 index-1 表在序列化时会被省略
OMITTED_BMP_INDEX_1_LENGTH = 0x10000 >> SHIFT_1 

# index-2 块中的条目数（64=0x40）
INDEX_2_BLOCK_LENGTH = 1 << SHIFT_1_2 

# 用于获取 index-2 块内偏移量的低位掩码
INDEX_2_MASK = INDEX_2_BLOCK_LENGTH - 1 

# 索引数组值左移的位数
# 以牺牲紧凑性为代价，支持 16 位索引值的更大数据尺寸
# 要求数据块按 DATA_GRANULARITY 对齐
INDEX_SHIFT = 2 

# 数据块中的条目数（32=0x20）
DATA_BLOCK_LENGTH = 1 << SHIFT_2 

# 用于获取数据块内偏移量的低位掩码
DATA_MASK = DATA_BLOCK_LENGTH - 1 

# index-2 表中 U+D800..U+DBFF 部分存储前导代理码单元（code units）的值而非码点（code points）
# 前导代理码点（code points）的值使用这部分表进行索引
# 长度=32=0x20=0x400>>SHIFT_2（共有 1024=0x400 个前导代理）
LSCP_INDEX_2_OFFSET = 0x10000 >> SHIFT_2 
LSCP_INDEX_2_LENGTH = 0x400 >> SHIFT_2 

# 计算两个 BMP 部分的长度总和（2080=0x820）
INDEX_2_BMP_LENGTH = LSCP_INDEX_2_OFFSET + LSCP_INDEX_2_LENGTH 

# 2 字节 UTF-8 版本的 index-2 表从偏移量 2080=0x820 开始
# 长度固定为 32=0x20（对应前导字节 C0..DF），与 SHIFT_2 无关
UTF8_2B_INDEX_2_OFFSET = INDEX_2_BMP_LENGTH 
UTF8_2B_INDEX_2_LENGTH = 0x800 >> 6  # U+0800 是 2 字节 UTF-8 后的首个码点

# index-1 表（仅用于补充码点）从偏移量 2112=0x840 开始
# 可变长度，范围直到 highStart（最后一个单值区间开始的位置）
# 最大长度 512=0x200=0x100000>>SHIFT_1（对应 0x100000 个补充码点 U+10000..U+10ffff）

# 补充码点的 index-2 表部分在此 index-1 表之后开始

# 如果只有 BMP 数据，index-1 表和后续的 index-2 表部分会被完全省略
INDEX_1_OFFSET = UTF8_2B_INDEX_2_OFFSET + UTF8_2B_INDEX_2_LENGTH 

# 数据块的对齐大小，也是压缩的粒度单位
DATA_GRANULARITY = 1 << INDEX_SHIFT 

class UnicodeTrie:
    def __init__(self, data):
        # 读取二进制格式数据
        self.highStart = struct.unpack_from('<I', data, 0)[0]  # 小端序读取高位起始值
        self.errorValue = struct.unpack_from('<I', data, 4)[0]  # 小端序读取错误值
        # uncompressedLength = struct.unpack_from('<I', data, 8)[0]  # 获取未压缩长度
        data = data[12:]  # 切分头部数据

        # 双重解压实际数据
        data = zlib.decompress(data, -zlib.MAX_WBITS)
        # 第二次解压（使用相同参数）
        data = zlib.decompress(data, -zlib.MAX_WBITS)

        self.data = struct.unpack(f'<{len(data)//4}I', data)  # 直接使用小端序，就不需要 swap32le 了

    def get(self, codePoint):
        if (codePoint < 0) or (codePoint > 0x10ffff):
            return self.errorValue  # 非法码点返回错误值

        if (codePoint < 0xd800) or ((codePoint > 0xdbff) and (codePoint <= 0xffff)):
            # 普通 BMP 码点（排除前导代理）
            # BMP 使用单层查找，索引从偏移量0开始，数据直接存储在索引数组中
            index = (self.data[codePoint >> SHIFT_2] << INDEX_SHIFT) + (codePoint & DATA_MASK) 
            return self.data[index] 

        if codePoint <= 0xffff:
            # 前导代理码点：有专门索引区域
            # 主索引存储代理码单元数据，此处需要码点数据
            index = (self.data[LSCP_INDEX_2_OFFSET + ((codePoint - 0xd800) >> SHIFT_2)] << INDEX_SHIFT) + (codePoint & DATA_MASK) 
            return self.data[index]

        if codePoint < self.highStart:
            # 补充码点使用双层查找
            index = self.data[(INDEX_1_OFFSET - OMITTED_BMP_INDEX_1_LENGTH) + (codePoint >> SHIFT_1)] 
            index = self.data[index + ((codePoint >> SHIFT_2) & INDEX_2_MASK)] 
            index = (index << INDEX_SHIFT) + (codePoint & DATA_MASK) 
            return self.data[index] 

        # 高位区间返回最后一个数据块的固定值
        return self.data[len(self.data) - DATA_GRANULARITY] 
