from jhx.ec import *
empty_dict = {}    # 空字典（散列表）
English_word = {
    'App':'应用；软件（一般指电子产品）',
    'China':'中国',
    'I':'我',
    'INS':'逆天团队',
    'ISS':'国际空间站',
    'a':'一；一个（表示一个、一块、一只、一条等的数量词）',
    'about':'关于；大约；与what/how连用(what/how about)时为“怎么样”',
    'according':'给予；赠予；授予；一致',
    'act':'动作；行为；举止；行动',
    'adventure':'探险；历险；冒险',
    'afraid':'对……害怕；惧怕；恐惧',
    'after':'在……之后',
    'along':'沿着；顺着；靠着……边；沿着……的某处(或旁边)；向前；一起；越来越',
    'always':'(频率副词)一直；总是',
    'am':'是(配合第一人称)',
    'an':'一；一个（表示一个、一块、一只、一条等的数量词）',
    'ant':'蚂蚁',
    'appear':'加入',
    'append':'加入',
    'apple':'苹果(一种水果)；苹果公司',
    'arm':'手臂',
    'arrive':'到达；抵达；送达；寄到；发生；到来',
    'arrow':'箭；箭头',
    'art':'美术；艺术；文艺',
    'article':'文章',
    'as':'像；如同；作为；当作；(比较时用)像…一样，如同；(指事情以同样的方式发生)和…一样；当…时；正如；尽管',
    'ask':'问；询问',
    'astronaut':'宇航员',
    'attack':'攻击；打击',
    'aunt':'阿姨；舅妈；姑姑；伯母',
    'away':'离开；去别处；不在；持续地；直到完全消失',
    'axe':'斧头',
    'axis':'轴；轴心；坐标轴(x,y,z,t,u,i,a,b等)；对称轴',
    'back':'背；回来；回到',
    'bad':'坏的；糟糕的；差的；情况不好的；烂的；难受的；严重的(贬)',
    'bag':'包包；书包(schoolbag，属于bag的一种)；背包',
    'balloon':'气球',
    'bear':'熊',
    'beef':'牛肉',
    'begin':'开始',
    'bike':'自行车',
    'black':'黑色的',
    'blue':'蓝色(一般指纯蓝，rgb值=0,0,255)',
    'boom':'爆炸；爆炸声',
    'box':'箱子',
    'brown':'棕色的',
    'bug':'臭虫；程序中的关键错误以及问题',
    'calculator':'计算器',
    'can':'(情态动词)可以；能；会；行',
    'candy':'糖果',
    'car':'小汽车；轿车',
    'carrot':'胡萝卜',
    'carry':'拿；带',
    'cat':'猫',
    'catch':'抓住；抓',
    'change':'改变；变化；变动；使……发生变化；调整；更改；更换；转换；变换；替代；变革；换',
    'check':'检查；审查；核查；检验；查明；查看；核实；控制；抑制；阻止',
    'chicken':'鸡；鸡肉',
    'child':'孩子；儿童；小孩；幼儿',
    'choice':'选择(自由选择，无选项)',
    'choose':'选择(有选项的挑选)',
    'circle':'圆；正圆形',
    'class':'课；班级；上课',
    'click':'点击；敲击',
    'clone':'克隆；生物克隆技术',
    'cloud':'云；云彩；云朵；信息学上的云技术',
    'club':'俱乐部',
    'code':'编码；编程',
    'coke-cola':'(简:cola)可口可乐',
    'cola':'(全:coke-cola)可口可乐',
    'cold':'冷的；感冒的',
    'collide':'碰撞；冲突',
    'column':'列；纵向',
    'computer':'电脑；计算机',
    'configure':'设置；配置',
    'congratulation':'祝贺',
    'correct':'对的；正确的；准确的',
    'cough':'咳嗽的',
    'cut':'切',
    'cute':'萌的；可爱的',
    'data':'数据',
    'date':'日期',
    'day':'天；日(24小时)',
    'define':'定义',
    'dentist':'牙医',
    'dictionary':'字典；词典',
    'die':'死；死的；去世的',
    'dirty':'脏的；肮脏的',
    'display':'显示(多用于电子产品)',
    'distance':'距离',
    'do':'做；干；(无意义的助动词)',
    'doctor':'医生',
    'dot':'点；圆点',
    'dragon':'龙',
    'draw':'绘画；绘图；绘制',
    'dress':'连衣裙',
    'drop':'水滴；水滴状；掉落',
    'dry':'干燥的',
    'duck':'鸭子',
    'east':'东方',
    'easy':'简单的',
    'eat':'吃(强调动作)',
    'ellipse':'椭圆',
    'excited':'激动的；兴奋的(形容人)',
    'exciting':'令人激动的；令人兴奋的(形容事物)',
    'eye':'眼睛',
    'fair':'美丽的',
    'fan':'扇子；粉丝',
    'file':'文件；文档',
    'fire':'火；火焰',
    'flash':'闪光',
    'fresh':'新鲜的',
    'fridge':'冰箱',
    'fun':'有趣的；有意思的',
    'gate':'大门',
    'goat':'山羊',
    'grass':'草(一种植物)',
    'green':'绿色的(一般指纯绿，rgb值=0,255,0)',
    'ha':'拟声词：笑声',
    'hate':'讨厌的',
    'he':'他',
    'hello':'你好（礼貌用语）',
    'hero':'英雄',
    'him':'他(宾格)',
    'hippopotomonstrosesquippedaliophobia':'长单词恐惧症',
    'hour':'小时',
    'infinity':'无穷大；无数；数不清的巨大数量；无限(∞)',
    'interesting':'有趣的',
    'jacket':'夹克衫',
    'jam':'果酱',
    'jhx':'小轩真名简写；jhx python库',
    'kangaroo':'袋鼠',
    'kid':'孩子；小孩；儿童',
    'kind':'种类；类别；友善的；慈祥的；慷慨的；友好的；宽容的',
    'koala':'考拉',
    'laugh':'大笑；嘲笑',
    'let':'让',
    'light':'灯；灯光',
    'list':'列表；菜单',
    'long':'长的',
    'many':'很多；许多(描述可数名词)',
    'mark':'成绩；分数；得分；痕迹',
    'me':'我(宾格)',
    'much':'很多；许多(描述不可数名词)',
    'my':'我的',
    'national':'国家的',
    'next':'接着；下一个',
    'no':'不；不是；没有',
    'nose':'鼻子',
    'not':'不；没有',
    'ocean':'海洋',
    'on':'(方位介词)在……之上，上面',
    'our':'我们的',
    'pass':'合格；通过；及格线',
    'pink':'粉色的',
    'point':'点；重点；小数点；圆点；[point at 指着；指向]',
    'point at':'指着；指向',
    'purple':'紫色的',
    'queen':'皇后；女王',
    'quick':'迅速的；快的',
    'quiet':'安静的',
    'rectangle':'矩形；长方形',
    'red':'红色的(一般指大红色，rgb值=255,0,0)',
    'run':'跑步',
    'seldem':'很少',
    'she':'她',
    'sheep':'羊；绵羊',
    'sleep':'睡觉',
    'square':'正方形',
    'start':'开始',
    'sweet':'甜的；糖果；甜蜜的',
    'test':'测试；考试',
    'thank':'谢谢',
    'the':'这；这个；这些；那；那个；那些',
    'the PRC':'中华人民共和国',
    'the UK':'英国',
    'the US':'美国',
    'the USA':'美国',
    'these':'那些',
    'think':'想',
    'traffic':'交通',
    'traffic jam':'交通堵塞',
    'train':'火车',
    'triangle':'三角形',
    'uncle':'叔叔；伯伯；舅舅；姑父；姨夫',
    'under':'(方位介词)在……下方',
    'value':'值；价值；数值',
    'very':'很，非常',
    'want':'想；想要(通常后面+to+动词原形)',
    'white':'白色的',
    'window':'窗户；视窗；窗口',
    'x-ray':'X光',
    'xerox':'复印',
    'yellow':'黄色的(一般指纯黄，rgb值=255,255,0)',
    'yes':'是；是的；对的；表示同意；正确的',
    'you':'你；你们',
    'your':'你的；你们的',
    'zebra':'斑马(动物)',
    'zoo':'动物园',
    'float':'浮点数，小数，漂浮物',
    'follow':'遵循，遵守，跟着',
    'number':'数，数字',
    'line':'线，队伍，行',
    'row':'行，横向',
    'sorry':'抱歉；对不起',
    'shh':'嘘',
    'ah':'啊',
    'hi':'你好；嗨',
    'have':'有；拥有；吃；喝；做；表示干某件事',
    'that':'那个',
    'this':'这个',
    'those':'那些',
    'play':'玩；打；戏剧',
    'theatre':'歌、剧院',
    'fly':'飞',
    'lose':'丢失',
    'find':'找到',
    'absolute':'绝对的',
    'king':'国王',
    'kill':'杀；杀死',
    'Art':'艺术',
    'PE':'体育',
    'Chinese':'中文；中国人；中国的；语文',
    'English':'英语（课）',
    'Maths':'数学',
    'paint':'画画，涂鸦',
    'drive':'驾驶',
    'root':'根；根部',
    'might':'力量；可能',
    'might be':'可能是',
    'may':'可能',
    'maybe':'可能是',
    'look for':'寻找',
    'look after':'照顾',
    'look at':'看向；看着',
    'point at':'指着；指向',
    'take':'拿；带；吃（药）',
    'task':'任务',
    'take care of':'照顾；照看',
}
jhx_good = [
    '只争朝夕，不负韶华',
    '简洁胜于复杂；复杂胜于凌乱；扁平胜于嵌套',
    '天无绝人之路',
    '相信相信的力量',
    '是金子总会发光',
    ]
jhx_write = [
    '在空间中的我直至时间，在时间中的我直至空间',
    '人生只为体验',
    ]

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
    return [x[1] for x in sort_data([(contrast_word(w,i),i) for i in l],'DOWN')]