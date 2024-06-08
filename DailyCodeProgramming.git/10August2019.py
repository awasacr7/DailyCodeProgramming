from functools import reduce
def MultipleNum(a):
    result=[]
    for i in range(len(a)):
        result.append(reduce((lambda x, y: x*y), (a[0:i]+a[i+1:len(a)])))
    return result

n=list(map(int,input().split()))
print(MultipleNum(n))