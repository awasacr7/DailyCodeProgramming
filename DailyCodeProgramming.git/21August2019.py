def longsubstring(st,k):
    lenstring=endindx=k
    strtindx=0
    while endindx<len(st):
        endindx+=1
        while True:
            d=len(set(st[strtindx:endindx]))
            if d<=k:
                break
            strtindx+=1
        lenstring=max(lenstring,endindx-strtindx)
    return lenstring

print(longsubstring('abcba',2))