#作答区域：补充第8行，第28行和第38行程序
from sklearn.naive_bayes import *
from sklearn.model_selection import *
import pandas as pd

c = GaussianNB()

df = pd.read_excel('data2.xlsx')

data = train_test_split(df[['年龄', '长度', '宽度', '步长', '步宽', '边缘是否完整', '型号']],df['性别'])
x_train = data[0]
x_test = data[1]
y_train = data[2]
y_test = data[3]

c.fit(x_train, y_train)
real = [[17, 27.0, 10.1250, 76.950,17.5,0,  2.0]]
res = c.predict(real)
print(res)
pro = c.predict_proba(real)
print(pro)

