from threading import *
from time import *

class Myclass:
    def __init__(self):
        self.data=0
        self.flag=False
        self.l=Lock()

    def put(self,d):
        while self.flag!=False:
            # print()
            pass
        self.l.acquire()
        self.data=d
        self.flag=True
        self.l.release()
    
    def get(self):
        while self.flag!=True:
            # print()
            pass
        self.l.acquire()
        x=self.data
        self.flag=False
        self.l.release()
        return x
    def produver(d): #object of my  class
        i=1
        while True:
            d.put(i)
            print('Producer: ',i)
            i+=1
            sleep(x)
    
    def Customer(d):
        while True:
            x=d.get()
            print('Customer: ',x)
    
m=Myclass()
t1=Thread(target=lambda:producer(m))
t2=Thread(target=lambda:Customer(m))
