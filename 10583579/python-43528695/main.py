"""
原题：
已知直角三角形三边长为整数，有一条边为85，求另两边长.

答案：
① 13, 84, 85
② 36, 77, 85
③ 40, 75, 85
④ 51, 68, 85
⑤ 85, 132, 157
⑥ 85, 204, 221
⑦ 85, 720, 725
⑧ 85, 3612, 3613

本程序可以求出
已知直角三角形三边长为整数，有一条边为给定的任意正整数，求另两边长.
"""

from typing import Optional,Union,List,Tuple
from math import sqrt,ceil
from random import randint
from time import time
from functools import lru_cache

t = time()

class Solution:
    def __init__(self) -> None:
        pass
    
    def get_prime_num(self, begin:Optional[int] = 1, end:Union[int,float,None] = float('inf')) -> int:
        num = begin
        while num <= end:
            if self.miller_rabbin(num):
                yield num
            num += 1
    
    @lru_cache(128)
    def miller_rabbin(self, target:int) -> bool:
        if target == 2 or target == 3:
            return True
        elif target == 1 or not target&1:
            return False
        m,times = target-1,0
        while not m&1:
            times += 1
            m >>= 1
        for _ in range(40):
            a = randint(2,target-1)
            last = self.__ksm(a,m,target)
            if last == 1:
                continue
            for i in range(times):
                res = self.__ksc(last,last,target)
                if res == 1 and last != target-1 and last != 1:
                    return False
                last = res
            if res != 1:
                return False
        return True

    @lru_cache(128)
    def __ksc(self, a:int, b:int, mod:int) -> int:
        res = 0
        while b:
            if b&1:
                res += a
                if res >= mod:
                    res -= mod
            a <<= 1
            a = a % mod
            b >>= 1
        return res
    
    @lru_cache(128)
    def __ksm(self, a:int, n:int, p:int) -> int:
        res = 1
        while n:
            if n&1:
                res = self.__ksc(res,a,p)
            a = self.__ksc(a,a,p)
            n >>= 1
        return res

    def factorization_prime_factor(self, target:int) -> List[int]:
        stopIdx = ceil(sqrt(target))
        res = []
        tmp = self.get_prime_num()
        num = 0
        while target != 1 and num < stopIdx:
            num = next(tmp)
            while target%num == 0:
                res.append(num)
                target /= num
        if target != 1:
            res.append(int(target))
        return res
    
    def permute_prime_factor(self, target:int) -> List[Tuple[int]]:
        res = []
        path = 1
        tmp = self.factorization_prime_factor(target)
        _tmp = list(set(tmp))
        _tmp.sort()
        def dfs(i:int) -> None:
            nonlocal path
            if i == len(_tmp):
                res.append(int(path))
                return
            for exponent in range(tmp.count(_tmp[i])+1):
                path *= _tmp[i]**exponent
                dfs(i+1)
                path /= _tmp[i]**exponent
        dfs(0)
        return sorted(res)
    
    def __judge1(self,target:int) -> List[Tuple[int]]:
        """
        判断本原勾股数中 `x = 2ab` 的情况
        """
        if target & 1:
            return []
        tmp = self.permute_prime_factor(target//2)
        res = []
        for i in range(len(tmp)//2):
            if tmp[-i-1] > tmp[i]:
                res.append((tmp[-i-1],tmp[i],self.edge//target))
            else:
                res.append((tmp[i],tmp[-i-1],self.edge//target))
        return res
    
    def __judge2(self,target:int) -> List[Tuple[int]]:
        """
        判断本原勾股数中 `y = a²-b²` 的情况
        则 y = (a+b)(a-b)
        即可枚举求出 a+b 和 a-b
        在逐个求出 a 和 b
        """
        tmp = self.permute_prime_factor(target)
        res = []
        for i in range(len(tmp)//2):
            a_plus_b = tmp[-i-1]
            a_minus_b = tmp[i]
            b = (a_plus_b - a_minus_b)/2
            if not float.is_integer(b):
                continue
            b = int(b)
            a = a_plus_b - b
            if a < b:
                a,b = b,a
            res.append((a,b,self.edge//target))
        return res

    def __judge3(self,target:int) -> List[Tuple[int]]:
        """
        判断本原勾股数中 `z = a²+b²` 的情况
        """
        res = []
        for i in range(1,int(sqrt(target)+1)):
            tmp = sqrt(target - i**2)
            if float.is_integer(tmp):
                if (i,int(tmp)) not in res and tmp != 0 and i != int(tmp):
                    if int(tmp) > i:
                        res.append((int(tmp),i,self.edge//target))
                    else:
                        res.append((i,int(tmp),self.edge//target))
        return res
    
    def edges_of_triangle(self,edge:int) -> List[Tuple[int]]:
        self.edge = edge
        res = []
        for i in self.permute_prime_factor(edge):
            res += self.__calc_the_res(self.__judge1(i))
            res += self.__calc_the_res(self.__judge2(i))
            res += self.__calc_the_res(self.__judge3(i))
        for item in res:
            while res.count(item) != 1:
                res.remove(item)
        res.sort()
        return res
    
    def __calc_the_res(self,i:Tuple[int]) -> List[Tuple[int]]:
        res = []
        for item in i:
            res.append(tuple(sorted((item[2]*2*item[0]*item[1],item[2]*(item[0]**2-item[1]**2),item[2]*(item[0]**2+item[1]**2)))))
        return res
        
sol = Solution()

# 算出前25个素数(1-100中的所有素数)
# fn = sol.get_prime_num()
# for i in range(25):
#     print(next(fn))

print("示例1:85")
print(sol.edges_of_triangle(85))
print("\n示例2:12")
print(sol.edges_of_triangle(12))
print(f"用时{time()-t}秒")

"""

### 前置知识 ###

1.本原勾股数
  若 x = 2ab
     y = a²-b²
     z = a²+b²
  (a,b为不相同的任意正整数,且满足a>b)
  则有 x² + y² = z²

2.miller-rabbin算法
  一种精确度极高的判定素数方法

"""