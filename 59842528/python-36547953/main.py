class Stack():
    def __init__(self):
        self.__array = []
    def push(self,content):
        self.__array.append(content)
    def size(self):
        return len(self.__array)
    def top(self):
        return self.__array[self.size()-1]
    def pop(self):
        del self.__array[self.size()-1]
    def empty(self):
        if(self.size()<=0):
            return True
        return False
    def out(self):
        for i in range(len(self.__array)):
            print(self.__array[i],end=" ")
        print("\n")
class Queue():
    def __init__(self):
        self.__array = []
    def push(self,content):
        self.__array.append(content)
    def size(self):
        return len(self.__array)
    def pop(self):
        for i in range(self.size()-1):
            self.__array[i]=self.__array[i+1]
    def front(self):
        return self.__array[0]
    def back(self):
        return self.__array[self.size()-1]
    def empty(self):
        if self.size()<=0:
            return True
        return False
    def out(self):
        for i in range(self.size()):
            print(self.__array[i],end=" ")
        print("\n") 
    
s="545*+5/"
mst=Stack()
for i in range(len(s)):
    
    if ord(s[i])>=ord("0") and ord(s[i])<=ord("9"):
        mst.push(ord(s[i])-ord('0'))
    else:
        num2 = mst.top();
        mst.pop();
        num1 = mst.top();
        mst.pop();
        if s[i]=='+' :
            mst.push(num1+num2);
        elif s[i]=='-' :
            mst.push(num1-num2);
        elif s[i]=='*' :
            mst.push(num1*num2);
        elif s[i]=='/' :
            mst.push(num1/num2);
print(mst.top())	
	
	
	

info=[
    [1,1,0,0,0],
    [0,1,1,1,1],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,0,1,1]
]
r,c=4,4

wayx,wayy = [0,-1,0,1],[-1,0,1,0]

mqu=Queue()

mqu.push([0,0,0])
info[0][0] = 1

isFind=False

while mqu.empty()==0 and isFind!=True:
    top=mqu.front()
    mqu.pop()
    for i in range(4):
	    nx = top[0]+ wayx[i]
	    ny = top[1]+ wayy[i]
	    if nx >= 0 and nx <= r and ny >= 0 and ny <= c and info[nx][ny]==1:
	        mqu.push([nx,ny,top[2]+1])
	        info[nx][ny] = 0;
	        if nx == r and ny == c:
	            print(top[2]+1)
	            isFind=True
	            break
if isFind==False:
    print("Can't find anyway")	        
