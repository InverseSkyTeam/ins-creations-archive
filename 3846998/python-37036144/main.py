class getchar_t:
    def __init__(self):
        self.s=""
    def getchar(self):
        if self.s=="":
            self.s=input()+"\n"
        ans=self.s[0]
        self.s=self.s[1:]
        return ans
getchar_t_instance=getchar_t()
getchar=getchar_t_instance.getchar
print(repr(getchar()+getchar()+getchar()))