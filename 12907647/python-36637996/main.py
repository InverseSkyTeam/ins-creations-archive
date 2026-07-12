import jieba

# 稍后添加
# 0分、不及格、讨厌、傻、烦恼、嫉妒、痛恨、可恶、憎恶、喜欢、爱、轻蔑

# 普通情绪
happy = 0 # 开心
sad = 0  # 难过
angry = 0  # 生气
afraid = 0  # 害怕、担心

# 专业情绪
contempt = 0  # 轻蔑
like = 0 # 喜爱
abhor = 0  # 憎恶、痛恨
jealousy = 0  # 嫉妒

# 普通词汇
wordlist = {
    '开心':[10,0,0,0,0,3,0,0],
    '高兴':[10,0,0,0,0,2,0,0],
    '快乐':[7,0,0,0,0,3,0,0],
    '好':[5,0,0,0,0,8,0,0],
    '棒':[8,0,0,0,0,5,0,0],
    '难受':[0,8,1,3,0,0,1,0],
    '难过':[0,11,0,4,0,0,1,0],
    '哭':[0,10,0,5,0,0,0,0],
    '扫兴':[0,4,6,1,0,0,1,0],
    '惊讶':[1,0,1,2,0,1,0,1],
    '悲哀':[1,16,1,6,0,0,2,1],
    '生气':[0,1,10,1,2,0,2,1],
    '愤怒':[1,4,17,3,5,0,6,2],
    '气死':[0,6,26,6,4,0,10,1],
    '哈哈':[9,0,0,0,1,3,0,0],
    '呵呵':[8,0,1,0,4,1,0,0],
    '呜呜':[0,11,0,7,0,0,0,0],
    '垃圾':[0,2,11,1,6,0,4,1],
}

text = input('输入你想进行情感辨析的话:')
textlist = jieba.lcut(text)
for i in range(len(textlist)):
    t = i
    if '很' in textlist[i] or textlist[i-1] == '很':
        t = textlist[i].replace('很','')
        weight = 1.2
    if '非常' in textlist[i] or textlist[i-1] == '非常':
        t = textlist[i].replace('非常','')
        weight = 1.5
    if '尤其' in textlist[i] or textlist[i-1] == '尤其':
        t = textlist[i].replace('尤其','')
        weight = 1.6
    if '特别' in textlist[i] or textlist[i-1] == '特别':
        t = textlist[i].replace('特别','')
        weight = 1.7
    if '异常' in textlist[i] or textlist[i-1] == '异常':
        t = textlist[i].replace('异常','')
        weight = 1.7
    if '极' in textlist[i] or textlist[i-1] == '极':
        t = textlist[i].replace('极','')
        weight = 2
    if '极为' in textlist[i] or textlist[i-1] == '极为':
        t = textlist[i].replace('极为','')
        weight = 2
    if '超级' in textlist[i] or textlist[i-1] == '超级':
        t = textlist[i].replace('超级','')
        weight = 2
    if t in wordlist:
        happy += wordlist[t][0]*weight
        sad += wordlist[t][1]*weight
        angry += wordlist[t][2]*weight
        afraid += wordlist[t][3]*weight
        contempt += wordlist[t][4]*weight
        like += wordlist[t][5]*weight
        abhor += wordlist[t][6]*weight
        jealousy += wordlist[t][7]*weight
print('分析结果:')
print('开心',happy)
print('难过',sad)
print('生气',angry)
print('害怕',afraid)
print('轻蔑',contempt)
print('喜爱',like)
print('憎恶',abhor)
print('嫉妒',jealousy)
print('\n感谢使用情感辨析器V0.2，它凝聚了很、非常这类词语，并且有18条情感词条，词条会慢慢增多')