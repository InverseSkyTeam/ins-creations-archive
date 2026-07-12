from xes.weather import *
def temp_get(cityname):
    temp = {
        1:'今天'+str(air_temp(cityname))+'℃',
        2:'明天'+str(air_temp(cityname,1))+'℃',
        3:'后天'+str(air_temp(cityname,2))+'℃',
        4:'大后天'+str(air_temp(cityname,3))+'℃',
        5:'第5天'+str(air_temp(cityname,4))+'℃',
        6:'第6天'+str(air_temp(cityname,5))+'℃',
        7:'第7天'+str(air_temp(cityname,6))+'℃',
        8:'第8天'+str(air_temp(cityname,7))+'℃',
        9:'第9天'+str(air_temp(cityname,8))+'℃',
        10:'第10天'+str(air_temp(cityname,9))+'℃',
    }
    return temp

def speed_get(cityname):
    speed = {
        1:'风速'+str(air_speed(cityname))+'m/s',
        2:'风速'+str(air_speed(cityname,1))+'m/s',
        3:'风速'+str(air_speed(cityname,2))+'m/s',
        4:'风速'+str(air_speed(cityname,3))+'m/s',
        5:'风速'+str(air_speed(cityname,4))+'m/s',
        6:'风速'+str(air_speed(cityname,5))+'m/s',
        7:'风速'+str(air_speed(cityname,6))+'m/s',
        8:'风速'+str(air_speed(cityname,7))+'m/s',
        9:'风速'+str(air_speed(cityname,8))+'m/s',
        10:'风速'+str(air_speed(cityname,9))+'m/s',
    }
    return speed