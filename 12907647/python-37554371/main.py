def findmost(text):
    insidelist = []
    indexlist = []
    insidetext = ''
    inside = 0
    index = -1
    for i in text:
        index += 1
        if i == '(':
            if inside == 0:
                insidetext = ''
                indexlist.append([index])
            else:
                insidetext += '('
            inside += 1
        elif i == ')':
            inside -= 1
            if inside == 0:
                insidelist.append(insidetext)
                indexlist[-1].append(index)
            else:
                insidetext += ')'
        else:
            insidetext += i
    return (insidelist,indexlist)
def has_inside(text):
    count = [0,0]
    for i in text:
        if i == '(':
            count[0] += 1
        elif i == ')':
            count[1] += 1
    if count[0] == count[1]:
        if count[0] == 0:
            return 'pass'
        return findmost(text)
    else:
        return False
print(has_inside('abc'))
print(has_inside('(123)'))
print(has_inside('a(bc)d'))
print(has_inside('(abc)d'))
print(has_inside('a(bcd)'))
print(has_inside('ab(c)dsl((s)l(s)s)(la)e(f)(g)123(64w)evt(g(0.)e(t)b)'))
print(has_inside('a(bc'))
print(has_inside('ab)c'))