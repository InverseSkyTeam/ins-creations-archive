import INSsimple
import cloudlib
print('加载中...')
d = eval(cloudlib.read_from_cloud('cloudaitdb',12907647))
count = 0
while 1:
    ask = input('你想说:')
    if ask in d:
        print('得到的回答:'+d[ask])
    else:
        print('恭喜，你的问题不在云数据库中，接下来的问题将有机会使你的数据采集至数据集')
        print('正在查找近似答案\n')
        answer = d[INSsimple.find_max_close_word(ask,d)]
        print('得到的回答:'+answer)
        ask2 = input('你会该回答满意吗?(输入y表示满意，输入其他则表示不满意)')
        if ask2 == 'y':
            print('谢谢你的参与，你的数据将会被采集到数据库，请稍等')
            d[ask] = answer
        else:
            ask3 = input('请输入你认为满意的回答:')
            print('很好，谢谢你的参与，你的数据将会被采集到数据库，请稍等')
            d[ask] = ask3
        count += 1
        print('恭喜你已经成为我们的预览成员了')
        ask4 = input('是否继续参与(输入y表示是，输入其他则表示否)')
        if ask4 == 'y':
            print('好的，谢谢，接下来将继续参与')
        else:
            print('感谢你从参与，正在统计数据...')
            cloudlib.save_to_cloud('cloudaitdb',str(d),12907647)
            print('你的数据保存完毕，感谢你的贡献')
            print('你的预览成员号码:',count,'\n请回复至评论区')
            break
    print('\n\n\n')