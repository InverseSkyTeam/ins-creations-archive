import math
import random
import time

get_p = lambda: round(random.uniform(-1,1),6)
for i in range(5): print(f'概率对比度: {([sum([get_p() for i in range(500)])/500 > 0 for i in range(200)].count(True)/2)}%')

HOLE_SIZE_MINN = 25
HOLE_SIZE_MAXN = 1600
NEXT_HOLE_SIZE_MINN = 10
NEXT_HOLE_SIZE_MAXN = 310

hole_size = random.randint(HOLE_SIZE_MINN,HOLE_SIZE_MAXN)
print(f'\033[40m+{"-"*57}+\n! 洞穴数据预算一览表{" "*38}!\n\033[40m+{"-"*57}+\n|\033[1;4;32m洞穴大小总数\033[0m\033[40m | \033[1;4;33m洞穴下一步数\033[0m\033[40m | \033[1;4;34m列偏移概率数\033[0m\033[40m | \033[1;4;35m行偏移概率数\033[0m\033[40m|')

while hole_size:
    next_hole_size = min(random.randint(NEXT_HOLE_SIZE_MINN,NEXT_HOLE_SIZE_MAXN),hole_size)
    offset_col = get_p()
    offset_row = get_p()
    
    ptf = f'|\033[1;32m{hole_size:<12d}\033[0m\033[40m | \033[1;33m{next_hole_size:<12d}\033[0m\033[40m | \033[1;34m{offset_col:12f}\033[0m\033[40m | \033[1;35m{offset_row:12f}\033[0m\033[40m|'
    print(ptf)
    
    hole_size -= next_hole_size

ptf = f'|\033[1;32m{hole_size:<12d}\033[0m\033[40m | \033[1;33m~\033[0m\033[40m            |            \033[1;34m~\033[0m\033[40m |            \033[1;35m~\033[0m\033[40m|'
print(ptf)
print(f'\033[40m+{"-"*57}+\033[0m')