from collections import deque

def maxarrsub(a,k):
    q=deque()
    for i in range(k):
        while q and a[i]>=a[q[-1]]:
            q.pop()
        q.append(i)
    
    for i in range(k,len(a)):
        print(a[q[0]])
        while q and q[0]<=i-k:
            q.popleft()
        while q and a[i]>=a[q[-1]]:
            q.pop()
        q.append(i)
    print(a[q[0]])

maxarrsub([19,15,12,7,8,7],3)