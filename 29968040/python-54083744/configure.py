import crafting

STONE = 1  # 石头
GRASS = 2  # 草方块
DIRT = 3  # 泥土
COBBLESTONE = 4  # 圆石
PLANKS = 5  # 木板
# SAPLING = 6  # 树苗
BEDROCK = 7  # 基岩
WATER = 8  # 水
# STATIONARY_WATER = 9  # 静止的水
# LAVA = 10  # 岩浆
# STATIONARY_LAVA = 11  # 静止的岩浆
SAND = 12  # 沙子
GRAVEL = 13  # 沙砾
GOLD_ORE = 14  # 金矿石
IRON_ORE = 15  # 铁矿石
COAL_ORE = 16  # 煤炭矿石
LOG = 17  # 原木
LEAVES = 18  # 树叶
SPONGE = 19  # 海绵
GLASS = 20  # 玻璃
RED_CLOTH = 21  # 红色羊毛
ORANGE_CLOTH = 22  # 橙色羊毛
YELLOW_CLOTH = 23  # 黄色羊毛
LIME_CLOTH = 24  # 黄绿色羊毛
GREEN_CLOTH = 25  # 绿色羊毛
AQUA_CLOTH = 26  # 淡蓝色羊毛
CYAN_CLOTH = 27  # 青色羊毛
BLUE_CLOTH = 28  # 蓝色羊毛
PURPLE_CLOTH = 29  # 紫色羊毛
INDIGO_CLOTH = 30  # 棕色羊毛
VIOLET_CLOTH = 31  # 淡灰色羊毛
MAGENTA_CLOTH = 32  # 品红色羊毛
PINK_CLOTH = 33  # 粉色羊毛
BLACK_CLOTH = 34  # 黑色羊毛
GREY_CLOTH = 35  # 灰色羊毛
WHITE_CLOTH = 36  # 白色羊毛
# YELLOW_FLOWER = 37  # 蒲公英
# RED_ROSE = 38  # 玫瑰
# BROWN_MUSHROOM = 39  # 棕色蘑菇
# RED_MUSHROOM = 40  # 红色蘑菇
GOLD_BLOCK = 41  # 金块
IRON_BLOCK = 42  # 铁块
DOUBLE_SLAB = 43  # 平滑石头
# SLAB = 44  # 平滑石台阶
BRICKS = 45  # 砖块
TNT = 46  # TNT
BOOKSHELF = 47  # 书架
MOSSY_COBBLESTONE = 48  # 苔石
OBSIDIAN = 49  # 黑曜石
# TORCH = 50  # 火把
# FIRE = 51  # 火
# MOB_SPAWNER = 52  # 刷怪笼
# WOODEN_STAIRS = 53  # 木台阶
CHEST = 54  # 箱子
# REDSTONE_WIRE = 55  # 红石粉
DIAMOND_ORE = 56  # 钻石矿石
DIAMOND_BLOCK = 57  # 钻石块
CRAFTING_TABLE = 58  # 工作台
# CROPS = 59  # 小麦
# SOIL = 60  # 耕地
FURNACE = 61  # 熔炉
LIT_FURNACE = 62  # 正在燃烧的熔炉
# SIGN_POST = 63  # TODO: 标志杆
# WOODEN_DOOR = 64  # 木门
# LADDER = 65  # 梯子
# RAILS = 66  # 铁轨
# COBBLESTONE_STAIRS = 67  # 圆石台阶
# SIGN = 68  # TODO: 标志
# LEVER = 69  # 拉杆，但贴图是圆石
# STONE_PRESSURE_PLATE = 70  # 石头压力板
# IRON_DOOR = 71  # 铁门
# WOODEN_PRESSURE_PLATE = 72  # 木质压力板
REDSTONE_ORE = 73  # 红石矿石
LIT_REDSTONE_ORE = 74  # 能发光的红石矿石
# REDSTONE_TORCH = 75  # 红石火把
# REDSTONE_TORCH_(OFF) = 76  # 熄灭的红石火把
# STONE_BUTTON = 77  # 石头按钮
# SNOW = 78  # 雪
# ICE = 79  # 冰
SNOW_BLOCK = 80  # 雪块
# CACTUS = 81  # 仙人掌
CLAY = 82  # 黏土块
# SUGAR_CANE = 83  # 甘蔗
JUKEBOX = 84  # 唱片机


CRAFTING = crafting.Crafting()
CRAFTING.add((LOG, None, None, None), (1, 0, 0, 0), PLANKS, 4)
CRAFTING.add((None, LOG, None, None), (0, 1, 0, 0), PLANKS, 4)
CRAFTING.add((None, None, LOG, None), (0, 0, 1, 0), PLANKS, 4)
CRAFTING.add((None, None, None, LOG), (0, 0, 0, 1), PLANKS, 4)
CRAFTING.add((PLANKS,)*4, (1,)*4, CRAFTING_TABLE, 1)
