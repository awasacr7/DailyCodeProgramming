#solution using set O(n) time complexity Linear Time Complexity
def LowPosNumv1(a):
    num=1
    st=set(a)
    for i in range(len(st)):
        if num in st:
            num+=1
    return num


#solution based on the result for searching the values Time Complexity O(n)
def LowPosNumv2(a):
    num=1
    while True:
        if num in a:
            num+=1
        else:
            return num

#solution with non-linear time complexity as sorting is used O(n log n)
def LowPosNumv3(a):
    num=1
    a.sort()
    a1=[i for i in filter(lambda x: x<0,a)]
    if len(a1)==len(a):
        return 1
    for i in range(len(a)):
        if num==a[i]:
            num=num+1
    return num


a=list(map(int,input().split()))
print(LowPosNumv2(a))