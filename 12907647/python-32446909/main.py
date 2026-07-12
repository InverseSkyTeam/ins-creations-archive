data = []
data2 = []
data3 = []
def ok(i,index1,index2,index3):                # 判断一个三角形的位置
    if i[index1-1] == i[index2-1] == i[index3-1]:
        return True
    
for i1 in [1,2]:   # 加入所有情况
    for i2 in [1,2]:
        for i3 in [1,2]:
            for i4 in [1,2]:
                for i5 in [1,2]:
                    for i6 in [1,2]:
                        for i7 in [1,2]:
                            for i8 in [1,2]:
                                for i9 in [1,2]:
                                    for i10 in [1,2]:
                                        for i11 in [1,2]:
                                            for i12 in [1,2]:
                                                for i13 in [1,2]:
                                                    for i14 in [1,2]:
                                                        for i15 in [1,2]:
                                                            data.append([i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15])

for i in data:
    # 判断有没有三角形
    if ok(i,1,2,4) or ok(i,1,11,15) or ok(i,1,12,14) or ok(i,1,3,5) or ok(i,8,2,11) or ok(i,8,4,15) or ok(i,8,7,13) or ok(i,8,6,9) or ok(i,10,3,5) or ok(i,10,5,14) or ok(i,10,13,6) or ok(i,10,7,9) or ok(i,5,7,11) or ok(i,4,6,12) or ok(i,2,5,13) or ok(i,2,6,14) or ok(i,3,4,13) or ok(i,3,7,15) or ok(i,9,11,14) or ok(i,9,12,15):
        data2.append(i) # 如果有，加入数据2
    else:
        data3.append(i) # 否则（没有）加入数据3
print(data3)     # 数据三为空，说明没有任何情况是没有单色三角形的（每种情况都有单色三角形）
print('空列表代表没有不出现单色三角形的可能，证明单色三角形定理一定。可以看源码')