import itertools,cardlist24 as c24

def twentyfour(list24):
    for nums in itertools.permutations(list24):
        for ops in itertools.product('+-*/', repeat=3):
            # 构造三种中缀表达式 (bsd)
            bds1 = '({0}{4}{1}){5}({2}{6}{3})'.format(*nums, *ops)
            bds2 = '(({0}{4}{1}){5}{2}){6}{3}'.format(*nums, *ops)
            bds3 = '{0}{4}({1}{5}({2}{6}{3}))'.format(*nums, *ops)
            
            for bds in [bds1, bds2, bds3]:
                try:
                    if abs(eval(bds) - 24.0) < 1e-10:
                        return bds
                except:
                    continue

card = [int(input('输入数字1：')),int(input('输入数字2：')),int(input('输入数字3：')),int(input('输入数字4：'))]
if card in c24.cards:
    print(twentyfour(card))
else:
    print('无解！')