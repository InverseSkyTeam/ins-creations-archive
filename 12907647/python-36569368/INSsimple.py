def hl_to_ll(l,times):
    '''high list to low list(^_^降维打击)'''
    times = int(times)
    if times == 2:
        return [j for i in l for j in i]
    else:
        return hl_to_ll([[j] if type(j) == int else j for i in l for j in i],times-1)

def sort_data(data,sortmode='UP'):
    '''数据排序'''
    if type(data) == dict:
        new_data = {}
        ld = len(data)
        while len(new_data) != ld:
            if sortmode == 'UP':
                md = min(data)
            else:
                md = max(data)
            new_data[md] = data[md]
            del data[md]
        return new_data
    if type(data) == list:
        new_data = []
        ld = len(data)
        while len(new_data) != ld:
            if sortmode == 'UP':
                md = min(data)
            else:
                md = max(data)
            new_data.append(md)
            data.remove(md)
        return new_data
    return False

def contrast_word(w1,w2):
    '''单词相似度对比'''
    w1 = list(w1)
    w2 = list(w2)
    l = [[None for j in w2] for i in w1]
    for i in range(len(w1)):
        for j in range(len(w2)):
            if w1[i] == w2[j]:
                if i == 0 or j == 0:
                    l[i][j] = 1
                else:
                    l[i][j] = l[i-1][j-1] + 1
            else:
                if i == 0 and j == 0:
                    l[i][j] = 0
                elif i == 0:
                    l[i][j] = l[i][j-1]
                elif j == 0:
                    l[i][j] = l[i-1][j]
                else:
                    l[i][j] = max([l[i][j-1],l[i-1][j]])
    return max(hl_to_ll(l,2))

def find_close_word(w,l):
    '''排序列表中与参数一最接近的单词'''
    return [x[1] for x in sort_data([(contrast_word(w,i)-abs(len(w)-len(i)),i) for i in l],'DOWN')]

def find_max_close_word(w,l):
    '''排序列表中与参数一最接近的单词'''
    return max([(contrast_word(w,i)-abs(len(w)-len(i)),i) for i in l])[1]