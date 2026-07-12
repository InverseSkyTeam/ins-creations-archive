n = int(input('精确值：'))
# 用小圆无限逼近
圆锥体积 = sum([i**2 for i in range(1,n+1)])
圆柱体积 = n**3
print(圆锥体积/圆柱体积)