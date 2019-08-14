class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def serialize(root):
    vals=[]
    def encode(node):
        vals.append(str(node.val))
        if node.left is not None:
            encode(node.left)
        else:
            vals.append('L')
        if node.right is not None:
            encode(node.right)
        else:
            vals.append('R')
    encode(root)
    print(vals)
    return vals

def deserialize(string_list):
    def create_a_tree(sub_list):
        if sub_list[0] == 'L' or sub_list[0] == 'R':
            del sub_list[0]
            return
        parent = Node(sub_list[0])
        del sub_list[0]
        parent.left = create_a_tree(sub_list)
        parent.right = create_a_tree(sub_list)
        return parent

    if len(string_list) != 0:
        root_node = create_a_tree(string_list)
    else:
        print("ERROR - empty string!")
        return 0

    return root_node

node = Node('root', Node('left', Node('left.left')), Node('right'))
t1=serialize(node)
t=deserialize(t1)
try:
    str(t.left.right.val)
except AttributeError:
    print('Value is None')