class Tridic:       # Tripledictionary
    def __init__(self,key,wkey,value):
        self.data = [key,wkey,value]
        self.type = "<class 'tripledictionary'>"
        self.dict = {self.data[0]:[self.data[1],self.data[2]]}
    def __str__(self):
        return 'Tripledictionary Class with https://code.xueersi.com/space/12907647'
    def get(self,tp='default'):
        if tp == 'default':
            return self.data
        else:
            redata = [i for i in self.data]
            redata.remove(tp)
            return redata
    def is_in_list(self,text):
        if text in self.data:
            return self.data.index(text)
        return False
    def is_in_part(self,text,index='no'):
        if index != 'no':
            if text in self.data[index]:
                return self.data[index]
        for part in self.data:
            if text in part:
                return part
        return False

d = Tridic('苏轼','赤壁怀古','大江东去浪淘尽，千古风流人物。')
print(d.get(d.is_in_part('大江东去浪淘尽')))
print(d.is_in_part('大江东去浪淘尽'))
print(d.is_in_part('赤壁'))
print(d.get('苏轼'))
print(d.get())
print(d.type)
print(d.dict)
print(str(d))
print('\n\n\n具体看源码')