class Base:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __call__(self):
        print('{}  {} '.format(self.x,self.y))
    def fmethod(self,x,y):
        self.z = x + y
        print('self.z {}'.format(self.z))

class Sub(Base):
    def __init__(self,a,b):
        super().__init__():
        self.a = a
        self.b = b
    def __call__(self):
        print('{}  {}'.format(self.a,self.b))
    def fmethod(self):
        self.c = self.a - self.b
        print('self.c  {}'.format(self.c))

if __name__ == 'moreclass':
    print __name__
    
