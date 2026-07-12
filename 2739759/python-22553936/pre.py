import pygame,sys
import csv
import jieba.analyse
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

def drop_stopwords(content_words,stopwords):
    content_words_clean = []
    for line_words in content_words:
        line_clean = []
        for word in line_words:
            if word in stopwords:
                continue
            line_clean.append(word)
        content_words_clean.append(line_clean)
    return content_words_clean

def prepare():
    df = pd.read_excel('gdata.xlsx',names=['category','content'])
    
    stopwords = pd.read_table('stopwords.txt',names=['stopword'],sep='\t',quoting=csv.QUOTE_NONE,encoding='UTF-8')
    stopwords = stopwords['stopword'].values.tolist()
    
    content = df['content'].values.tolist()
    
    content_words = []
    for line in content:
        current_segment = jieba.lcut(line)
        if len(current_segment) > 1 and current_segment != '\t\r':
            content_words.append(current_segment)
    
        
        
    content_words_clean = drop_stopwords(content_words,stopwords)
    train_data = pd.DataFrame({"content_clean":content_words_clean,"label":df['category']})
    label_mapping = {"王者荣耀": 1, "我的世界": 2}
    train_data['label'].unique()
    train_data['label'] = train_data['label'].map(label_mapping)
    
    
    x_train,x_test,y_train,y_test = train_test_split(train_data['content_clean'].values,train_data['label'].values,random_state=1)
    train_words = []
    for line_index in range(len(x_train)):
        train_words.append(' '.join(x_train[line_index]))
    train_words[0]
    
    test_words = []
    for line_index in range(len(x_test)):
        test_words.append(' '.join(x_test[line_index]))
    test_words[0]
    
    
    
    tv = TfidfVectorizer(analyzer='word',max_features=5000,lowercase=False)
    feature = tv.fit_transform(train_words)
    test_word = tv.transform(test_words)
    
    print("请输入游戏信息")
    test_content  = input()
    test_current_segment = jieba.lcut(test_content)
    test_contents_clean = drop_stopwords(content_words = [test_current_segment],stopwords=stopwords)
    t_words = [' '.join(test_contents_clean[0])]
    t_word = tv.transform(t_words)
    return feature, y_train, y_test, test_word, t_word
 
 
feature, y_train, y_test, test_word, t_word = prepare()

def x_train_get():
    return feature
    
def y_train_get():
    return y_train
    
def x_test_get():
    return test_word
    
def y_test_get():
    return y_test

def t_word_get():
    return t_word    
    
def show(res):
    
    if res == [1]:
        l2 = "Glory of Kings"
        print("王者荣耀")
    else:
        l2 = "Minecraft"
        print("我的世界")
        
        
        
    # pygame.init()
    # screen = pygame.display.set_mode((1000,600))
    # pygame.display.set_caption("我的作品")
    # myImg = pygame.image.load("4.jpg")
    # myFont = pygame.font.SysFont(None, 200)
    
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #     screen.fill((255,255,255))
    #     screen.blit(myImg,(0,0))
    #     textImage = myFont.render(l2, True, (255, 0, 0))
    #     screen.blit(textImage, (200, 300))
    #     pygame.display.update()
