from random import random
radius=2

def estimate(iters):
    counter=0
    raduissaq=radius**2
    for _ in range(iters):
        xcord=random()*radius
        ycord=random()*radius
        if xcord**2+ycord**2<raduissaq:
            counter+=1
    return 4*counter/iters

print('%.3f'%round(estimate(100000000),3))