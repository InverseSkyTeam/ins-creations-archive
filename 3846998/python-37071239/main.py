class getchar_t:
    def __init__(self):
        self.s=""
    def getchar(self):
        if self.s=="":
            self.s=input()+"\n"
        ans=self.s[0]
        self.s=self.s[1:]
        return ans
    def getstr(self):
        c=self.getchar()
        while c in "\n\t ":
            c=self.getchar()
        while c[-1] not in "\n\t ":
            c+=self.getchar()
        c=c[:-1]
        return c
    def getint(self):
        return int(self.getstr())
    def getline(self):
        c=self.getchar()
        while c[-1]!="\n":
            c+=self.getchar()
        return c[:-1]
getchar_t_instance=getchar_t()
getchar=getchar_t_instance.getchar
getstr=getchar_t_instance.getstr
getint=getchar_t_instance.getint
getline=getchar_t_instance.getline
print(getint())