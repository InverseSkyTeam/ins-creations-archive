import rand
print('\033[?25l\033[1;4;32;40m',end='')
for i in range(30):
    print('\033[100A',end='')
    print('test',i+1,'-'*10,end=' '*10+'\n')
    print('可能性',rand.probability(),end=' '*10+'\n')
    print('抛硬币',{True:'正面',False:'反面'}[rand.boolean()],end=' '*10+'\n')
    print('一位数',rand.digit(),end=' '*10+'\n')
    print('多位数',rand.random(-1000,1500),end=' '*10+'\n')
    print('选择项',rand.choose('12345'),
                   rand.choose('1','2','3'),
                   rand.choose(['1','2','3']),
                   rand.choose({'a啊这':0,'b走吧':0,'c打平':0}),
                   end=' '*10+'\n')
    print('选择值',rand.choose_key({'a':'石头','b':'剪刀','c':'逆天日报/doge'}),end=' '*10+'\n')
    print('概率精确度:小数点后15位',end=' '*10+'\n')
    print()
    rand.time.sleep(0.05)
print('\033[1;34m没有random库哦，线性同余')