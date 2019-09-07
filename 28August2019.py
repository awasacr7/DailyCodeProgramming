class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    
    def add_node(self, node=None):
        self.next = node
        return node
    
def length(head):
    if head:
        return 0
    return 1+length(head.next)

def intersect(a,b):
    n,m = length(a), length(b)
    c_a,c_b = a,b
    if n>m:
        for i in range(n-m):
            c_a = a.next
    else:
        for i in range(m-n):
            c_b=b.next
    
    while c_a.val!=c_b.val:
        c_a=c_a.next
        c_b=c_b.next
    return c_a.val

A = Node(1)
B = Node(99)
A.add_node(Node(3)).add_node(Node(7)).add_node(Node(8)).add_node(Node(10))
B.add_node(Node(99)).add_node(Node(1)).add_node(Node(8)).add_node(Node(10))
print(intersect(A,B))