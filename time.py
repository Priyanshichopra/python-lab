class time:
    def __init__(self):
        self.h=00
        self.m=00
        self.s=00
    def getTime(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
    def showTime(self):
        print(self.h,":",self.m,":",self.s)
t=time()
t.showTime()
t.getTime(11,58,9)
t.showTime()

        
