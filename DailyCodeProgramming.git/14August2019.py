import ctypes

class Node(object):
    def __init__(self,val):
        self.val = val
        self.both=0
    
class FinalAction(object):
    def __init__(self):
        self.head = self.tail = None
        self.__nodes = []
    
    def add(self,node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail = id(node) ^ self.tail.both
            node.both = id(self.tail)
            self.tail = node
        
        self.__nodes.append(node)
        
    def get(self,index):
        prev_node = 0
        node = self.head
        for i in range(index):
            next_node = prev_node ^ node.both
            
            if next_node:
                prev_node = id(node)
                node = _get_obj(next_node)
            else:
                raise IndexError("Out of Range")
        return node
    
def _get_obj(id):
    return ctypes.cast(id,ctypes.py_object).value

