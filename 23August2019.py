import random

def generate(l):
    for i,e in enumerate(l):
        if random.randint(1,i+1)==1:
            print(e)


l=[1,9,4,10,90,34,67,43,98]
generate(l)