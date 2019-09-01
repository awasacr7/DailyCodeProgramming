class Logging(object):
    def __init__(self,n):
        self.n = n
        self._order=[]
        self.curr=0 
    
    def record(self,order_id):
        if len(self._order)==self.n:
            self._order[self.curr]=order_id
        else:
            self._order.append(order_id)
        self.curr=(self.curr+1)%self.n
        
    def get_last(self,i):
        return self._order[self.curr-i]
    
l=Logging(15)
for i in range(1,16):
    l.record(i)
    
l.record(20)
print(l.get_last(2))