import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.charts import Radar
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.charts import Pie
from pyecharts.commons.utils import JsCode
import random,os
'''
li ：list of all
nl ：name_list
vl : view_list
ll ：likes_list
ull : umlikes_list
fl ：favorite_list
al : adaptation_list
cl : comment_list

'''
class Analysis():
    def __init__(self,body):
        self.all=body
        self.name_list=[]
        self.view_list=[]
        self.like_list=[]
        self.unlike_list=[]
        self.favorite_list=[]
        self.adaptation_list=[]
        self.comment_list=[]
        self.date=[]
        self.mainlyabout=["浏览","点赞","踩","收藏","改编","评论"]
    def read(self):
        for i in range(len(self.all)):
            self.name_list.append(self.all[i][0])
            self.view_list.append(self.all[i][1])
            self.like_list.append(self.all[i][2])
            self.unlike_list.append(self.all[i][3])
            self.favorite_list.append(self.all[i][4])
            self.adaptation_list.append(self.all[i][5])
            self.comment_list.append(self.all[i][6])
            self.date.append(self.all[i][7])
    def out(self):
        try:
            print(self.name_list)
            print(self.view_list)
            print(self.like_list)
            print(self.unlike_list)
            print(self.favorite_list)
            print(self.adaptation_list)
            print(self.comment_list)
            print(self.date)
            print("Run Successfully")
        except:
            print("Errow")
        
    def lineAnalysisAll(self):
        L = Line()
        L.add_xaxis(self.name_list)
        L.add_yaxis("观看数量", self.view_list,is_smooth=True,is_connect_nones=True,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            )
        )
        L.add_yaxis("点赞数量", self.like_list,is_smooth=True,is_connect_nones=True,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            )
        )
        L.add_yaxis("踩数量", self.unlike_list,is_smooth=True,is_connect_nones=True,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            )
        )
        L.add_yaxis("收藏数量", self.favorite_list,is_smooth=True,is_connect_nones=True,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            )
        )
        L.add_yaxis("改编数量", self.adaptation_list,is_smooth=True,is_connect_nones=True,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            )
        )
        L.add_yaxis("评论数量", self.comment_list,is_smooth=True,is_connect_nones=True,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            )
        )
        L.set_global_opts(title_opts=opts.TitleOpts(title="作品各项指标对比"),datazoom_opts=opts.DataZoomOpts(type_="slider"))#可筛选
        L.render("所有作品各项指标分析.html")
    def barContrast(self,list_for_contrast):
        b=Bar()
        b.add_xaxis(self.mainlyabout)
        content_list=[]
        for i in range(len(list_for_contrast)):
            content_list.append(self.all[i][1:7])
            b.add_yaxis(self.all[i][0],content_list[i])
        b.set_global_opts(title_opts=opts.TitleOpts(title="作品各项指标对比"),datazoom_opts=opts.DataZoomOpts(type_="slider"))#可筛选

        b.render("作品柱状对比图可筛选.html")    
    def pieContrast(self,list_for_contrast):#应该是个二维列表
        kindOfWork1=["原创","改编","转载"]
        kindOfWork2=["游戏","动画","故事","模拟","艺术","教程","算法","海龟","沙盒","网站","其他"]
        contentOfWork1=list_for_contrast[0]
        contentOfWork2=list_for_contrast[1]
        Data1=[]
        Data2=[]
        
        for i in range(3):
            Data1.append((kindOfWork1[i],contentOfWork1[i]))
        for i in range(11):
            Data2.append((kindOfWork2[i],contentOfWork2[i]))
        a = Pie()
        
        a.set_global_opts(title_opts = opts.TitleOpts(title=""))
        a.add("作品类型比例分析",Data1,radius=["30%", "50%"],center=["27%", "60%"])
        a.add("作品类型比例分析",Data2,radius=["30%", "50%"],center=["72%", "60%"])
        a.set_series_opts(label_opts=opts.LabelOpts(formatter="{b} :{c}\n百分比： {d}%"))
        

        
        
        a.render("各类型作品数量分析.html")

    def raderContrast(self,list_for_contrast):
        content_list=[]
        name_list=[]
        for i in range(len(list_for_contrast)):
            content_list.append(
                [ 
                    self.all[list_for_contrast[i]][1],
                    self.all[list_for_contrast[i]][2],
                    self.all[list_for_contrast[i]][4],
                    self.all[list_for_contrast[i]][5],
                    self.all[list_for_contrast[i]][6]
                ]
            )
            name_list.append(self.all[list_for_contrast[i]][0])

            for j in range(len(content_list[i])):
                if j==0:
                    if content_list[i][0] <10:
                        content_list[i][0]=1
                    elif content_list[i][0] <30:
                        content_list[i][0]=2
                    elif content_list[i][0] <50:
                        content_list[i][0]=3
                    elif content_list[i][0] <80:
                        content_list[i][0]=4
                    elif content_list[i][0] <100:
                        content_list[i][0]=5
                    elif content_list[i][0] <150:
                        content_list[i][0]=6
                    elif content_list[i][0] <300:
                        content_list[i][0]=7
                    elif content_list[i][0] <500:
                        content_list[i][0]=8
                    elif content_list[i][0] <1000:
                        content_list[i][0]=9
                    elif content_list[i][0] <1800:
                        content_list[i][0]=10
                    elif content_list[i][0] <3000:
                        content_list[i][0]=11
                    else:
                        content_list[i][0]=12
                if j==1:
                    if self.all[list_for_contrast[i]][1]!=0 and self.all[list_for_contrast[i]][2]!=0:
                        likerate=self.all[list_for_contrast[i]][1]%self.all[list_for_contrast[i]][2]
                    else:
                        likerate=0
                    if likerate <0.01:
                        content_list[i][1]=1
                    elif likerate <0.02:
                        content_list[i][1]=2
                    elif likerate <0.05:
                        content_list[i][1]=3
                    elif likerate <0.1:
                        content_list[i][1]=4
                    elif likerate <0.15:
                        content_list[i][1]=5
                    elif likerate <0.2:
                        content_list[i][1]=6
                    elif likerate <0.33:
                        content_list[i][1]=7
                    elif likerate <0.4:
                        content_list[i][1]=8
                    elif likerate <0.5:
                        content_list[i][1]=9
                    elif likerate <0.6:
                        content_list[i][1]=10
                    elif likerate <0.75:
                        content_list[i][1]=11
                    else:
                        content_list[i][1]=12
                if j==2:
                    if self.all[list_for_contrast[i]][1]!=0 and self.all[list_for_contrast[i]][4]!=0:
                        favoraterate=self.all[list_for_contrast[i]][1]%self.all[list_for_contrast[i]][4]
                    else:
                        favoraterate=0
                    if favoraterate <0.01:
                        content_list[i][2]=1
                    elif favoraterate <0.02:
                        content_list[i][2]=2
                    elif favoraterate <0.05:
                        content_list[i][2]=3
                    elif favoraterate <0.1:
                        content_list[i][2]=4
                    elif favoraterate <0.15:
                        content_list[i][2]=5
                    elif favoraterate <0.2:
                        content_list[i][2]=6
                    elif favoraterate <0.25:
                        content_list[i][2]=7
                    elif favoraterate <0.3:
                        content_list[i][2]=8
                    elif favoraterate <0.35:
                        content_list[i][2]=9
                    elif favoraterate <0.40:
                        content_list[i][2]=10
                    elif favoraterate <0.45:
                        content_list[i][2]=11
                    else:
                        content_list[i][2]=12
                if j==3:
                    if self.all[list_for_contrast[i]][1]!=0 and self.all[list_for_contrast[i]][5]!=0:
                        adaptationrate=self.all[list_for_contrast[i]][1]%self.all[list_for_contrast[i]][5]
                    else:
                        adaptationrate=0
                    if adaptationrate <0.01:
                        content_list[i][3]=1
                    elif adaptationrate <0.02:
                        content_list[i][3]=2
                    elif adaptationrate <0.05:
                        content_list[i][3]=3
                    elif adaptationrate <0.1:
                        content_list[i][3]=4
                    elif adaptationrate <0.15:
                        content_list[i][3]=5
                    elif adaptationrate <0.2:
                        content_list[i][3]=6
                    elif adaptationrate <0.25:
                        content_list[i][3]=7
                    elif adaptationrate <0.3:
                        content_list[i][3]=8
                    elif adaptationrate <0.35:
                        content_list[i][3]=9
                    elif adaptationrate <0.40:
                        content_list[i][3]=10
                    elif adaptationrate <0.45:
                        content_list[i][3]=11
                    else:
                        content_list[i][3]=12
                if j==4:
                    self.all[list_for_contrast[i]][6]
                    if adaptationrate <3:
                        content_list[i][4]=1
                    elif adaptationrate <5:
                        content_list[i][4]=2
                    elif adaptationrate <10:
                        content_list[i][4]=3
                    elif adaptationrate <15:
                        content_list[i][4]=4
                    elif adaptationrate <20:
                        content_list[i][4]=5
                    elif adaptationrate <30:
                        content_list[i][4]=6
                    elif adaptationrate <50:
                        content_list[i][4]=7
                    elif adaptationrate <75:
                        content_list[i][4]=8
                    elif adaptationrate <85:
                        content_list[i][4]=9
                    elif adaptationrate <100:
                        content_list[i][4]=10
                    elif adaptationrate <150:
                        content_list[i][4]=11
                    else:
                        content_list[i][3]=12
        c=Radar()
        c.add_schema(
                schema=[
                    opts.RadarIndicatorItem(name="浏览数量等级", max_=12),
                    opts.RadarIndicatorItem(name="点赞数量等级", max_=12),
                    opts.RadarIndicatorItem(name="收藏数量等级", max_=12),
                    opts.RadarIndicatorItem(name="改编数量等级", max_=12),
                    opts.RadarIndicatorItem(name="评论数量等级", max_=12),
                    
                ]
            )
        color_list=["#3B99D4", "#8ED14B", "#F06B49","#ECC2F1", "#82C7C3", "#E3698A","#1776EB", "#F5B2AC","#533085","#89363A","#19413E", "#D92B45", "#60C9FF", "#1B9F2E", "#BA217D","#076B82"]
        for i in range(len(list_for_contrast)):
            c.add(
                name_list[i],
                [content_list[i]],
                is_selected = True,
                areastyle_opts=opts.AreaStyleOpts(color=random.choice(color_list),opacity=0.2)
            )
            
        c.set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        c.set_global_opts(
            legend_opts=opts.LegendOpts(selected_mode="single"),
            title_opts=opts.TitleOpts(title="作品各项指标对比"),
        )
        c.render("作品综合六维雷达图分析指标.html")
    
        
'''
def Analysis_view(self):
        L = Line()
        L.add_xaxis(self.name_list)
        L.add_yaxis("观看数量", self.view_list,is_smooth=True,is_connect_nones=True,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            )
        )
        L.render("观看数量折线分析.html")
    def Analysis_like(self):
        L = Line()
        L.add_xaxis(self.name_list)
        L.add_yaxis("点赞数量", self.like_list,is_smooth=True,is_connect_nones=True,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            )
        )
        L.render("点赞数量折线分析.html")
    def Analysis_unlike(self):
        L = Line()
        L.add_xaxis(self.name_list)
        L.add_yaxis("踩数量", self.unlike_list,is_smooth=True,is_connect_nones=True,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            )
        )
        L.render("踩折线分析.html")
    def Analysis_favorite(self):
        L = Line()
        L.add_xaxis(self.name_list)
        L.add_yaxis("收藏数量", self.favorite_list,is_smooth=True,is_connect_nones=True,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            )
        )
        L.render("收藏数量折线分析.html")
    def Analysis_adaptation(self):    
        L = Line()
        L.add_xaxis(self.name_list)
        L.add_yaxis("改编数量", self.adaptation_list,is_smooth=True,is_connect_nones=True,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            )
        )
        L.render("改编数量折线分析.html")
    def Analysis_comment(self):
        L = Line()
        L.add_xaxis(self.name_list)
        L.add_yaxis("评论数量", self.comment_list,is_smooth=True,is_connect_nones=True,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            )
        )
        L.render("评论数量折线分析.html")
'''