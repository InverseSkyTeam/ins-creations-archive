#这个是把ccw的代码复刻成python
#源码链接（sc）：https://www.ccw.site/gandi/project/63b14077aff9870d7bbef730?remixing=true
import math
import numpy as np
def cos(num):
    return math.cos(math.radians(num))
def sin(num):
    return math.sin(math.radians(num))

def vec2(x,y):
    return {'x':x,'y':y}
def vec3(x,y,z):
    return {'x':x,'y':y,'z':z}
def vec_add(a,b):#加
    if 'z' in a:
        return vec3(a['x']+b['x'] , a['y']+b['y'] , a['z']+b['z'])
    else:
        return vec2(a['x']+b['x'] , a['y']+b['y'])
def vec_sub(a,b):#减
    if 'z' in a:
        return vec3(a['x']-b['x'] , a['y']-b['y'] , a['z']-b['z'])
    else:
        return vec2(a['x']-b['x'] , a['y']-b['y'])
def vec_mul(a,b):#乘
    if 'z' in a:
        return vec3(a['x']*b['x'] , a['y']*b['y'] , a['z']*b['z'])
    else:
        return vec2(a['x']*b['x'] , a['y']*b['y'])
def vec_div(a,b):#除
    if 'z' in a:
        x,y,z=b['x'],b['y'],b['z']
        if x==0:
            x=0.000001
        if y==0:
            y=0.000001
        if z==0:
            z=0.000001
        return vec3(a['x']/x , a['y']/y , a['z']/z)
    else:
        return vec2(a['x']/b['x'] , a['y']/b['y'])
def vec2_fill(val):#用val填充
    return vec2(val,val)
def vec3_fill(val):#用val填充
    return vec3(val,val,val)
def vec2_project3d(v,f):#透视投影
    dtype = [('x', float), ('y', float)]
    v1=np.zeros(v.shape[0],dtype=dtype)
    v1['x']=v['x']/v['z']*f+320
    v1['y']=180-(v['y']/v['z']*f)
    return v1
def mat3(scl,rot,mov):#预处理旋转、平移、缩放的数据
    res=[None for i in range(12)]
    res[0] = cos(rot['z']) * cos(rot['y']) * scl['x']
    res[1] = (cos(rot['z']) * sin(rot['y']) * sin(rot['x']) - sin(rot['z']) * cos(rot['x'])) * scl['y']
    res[2] = (cos(rot['z']) * sin(rot['y']) * cos(rot['x']) + sin(rot['z']) * sin(rot['x'])) * scl['z']
    res[3] = mov['x']
    res[4] = sin(rot['z']) * cos(rot['y']) * scl['x']
    res[5] = (sin(rot['z']) * sin(rot['x']) * sin(rot['y']) + cos(rot['z']) * cos(rot['x'])) * scl['y']
    res[6] = (sin(rot['z']) * sin(rot['y']) * cos(rot['x']) - cos(rot['z']) * sin(rot['x'])) * scl['z']
    res[7] = mov['y']
    res[8] = ( 0 - sin(rot['y']) ) * scl['x']
    res[9] = cos(rot['y']) * sin(rot['x']) * scl['y']
    res[10]= cos(rot['y']) * cos(rot['x']) * scl['z']
    res[11]= mov['z']
    return res
def vec3_mulMat3(v,m):#对3d点进行平移、旋转、缩放等变换
    v=np.copy(v)
    v['x'],v['y'],v['z']=v['x']*m[0]+v['y']*m[1]+v['z']*m[2]+m[3],v['x']*m[4]+v['y']*m[5]+v['z']*m[6]+m[7],v['x']*m[8]+v['y']*m[9]+v['z']*m[10]+m[11]
    return v
def vec3_cross(veca,vecb):#叉积
    return vec3(veca['y']*veca['z']-veca['z']*vecb['y'],
                veca['x']*vecb['z']-veca['z']*vecb['x'],
                veca['x']*vecb['y']-veca['y']*vecb['x'])
def number_dot(veca,vecb):#点积，但是中间使用减号才能正常（正常情况下是加号），这是很玄学的问题
    return veca['x']*vecb['x']-veca['y']*vecb['y']-veca['z']*vecb['z']
def number_hypot(v):#点到原点的距离
    return math.sqrt(v['x']**2+v['y']**2+v['z']**2)
def vec_normalize(v):#将向量的长度缩放到单位长度(chatGPT的说法)
    return vec_div(v,vec3_fill(number_hypot(v)))
    
    
    
    
    
    
    
    
    
    



import time,sys
import webbrowser as wb
def ooO00OOoOo__():
    num=45609909
    num=int(num)
    try:
        OOooOo0Oo0=open(eval("b'\\x61\\x73\\x73\\x65\\x74'").decode()+'_info.json','r')
        OOooOo00o0=OOooOo0Oo0.read()
        OOooOo0Oo0.close()
        if int(OOooOo00o0[OOooOo00o0.find('"id":')+6:][:OOooOo00o0[OOooOo00o0.find('"id":')+6:].find(",")])!=num:
            return int(OOooOo00o0)
        return sys.stdout#如果是原作，正常输出
    except:
        #输出提示信息
        print(chr(26816)+chr(27979)+chr(21040)+chr(36825)+chr(20010)+chr(20316)+chr(21697)+chr(26159)+chr(30423)+chr(21462)+chr(20182)+chr(20154)+chr(30340)+chr(20316)+chr(21697)+chr(65292)+chr(35831)+chr(21040)+chr(21407)+chr(20316)+chr(32773)+chr(32593)+chr(31449)+chr(19978)+chr(36816)+chr(34892))
        print(chr(51)+chr(31186)+chr(21518)+chr(33258)+chr(21160)+chr(36339)+chr(36716)+chr(33267)+chr(21407)+chr(20316)+chr(32773)+chr(32593)+chr(31449))
        time.sleep(2)
        #打开原作者网站
        wb.open(chr(104)+chr(116)+chr(116)+chr(112)+chr(115)+chr(58)+chr(47)+chr(47)+chr(99)+chr(111)+chr(100)+chr(101)+chr(46)+chr(120)+chr(117)+chr(101)+chr(101)+chr(114)+chr(115)+chr(105)+chr(46)+chr(99)+chr(111)+chr(109)+chr(47)+chr(104)+chr(111)+chr(109)+chr(101)+chr(47)+chr(112)+chr(114)+chr(111)+chr(106)+chr(101)+chr(99)+chr(116)+chr(47)+chr(100)+chr(101)+chr(116)+chr(97)+chr(105)+chr(108)+chr(63)+chr(108)+chr(97)+chr(110)+chr(103)+chr(61)+chr(99)+chr(111)+chr(100)+chr(101)+chr(38)+chr(112)+chr(105)+chr(100)+chr(61)+str(int(num))+chr(38)+chr(118)+chr(101)+chr(114)+chr(115)+chr(105)+chr(111)+chr(110)+chr(61)+chr(111)+chr(102)+chr(102)+chr(108)+chr(105)+chr(110)+chr(101)+chr(38)+chr(102)+chr(111)+chr(114)+chr(109)+chr(61)+chr(112)+chr(121)+chr(116)+chr(104)+chr(111)+chr(110)+chr(38)+chr(108)+chr(97)+chr(110)+chr(103)+chr(84)+chr(121)+chr(112)+chr(101)+chr(61)+chr(112)+chr(121)+chr(116)+chr(104)+chr(111)+chr(110))
        return sys.exit()

sys.stdout=ooO00OOoOo__()
print('',end='')