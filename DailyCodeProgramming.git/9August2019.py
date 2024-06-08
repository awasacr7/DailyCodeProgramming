def CheckSum(a,n):
    for i in range(len(a)):
        rem =  n-a[i]
        if rem in a:
            return True
    return False

a=list(map(int,input().split()))
n=int(input())
print(CheckSum(a,n))