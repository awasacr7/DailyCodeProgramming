def max_class(inter):
    start = sorted(s for s,e in inter)
    end = sorted(e for s,e in inter)
    # print(start,end)
    c_max ,  c_temp = 0 , 0
    i , j = 0 , 0
    while i < len(inter) and j <len(inter):
        if start[i] < end[j]:
            c_temp += 1
            c_max = max(c_max,c_temp)
            i+=1
        else:
            c_temp-=1
            j+=1
    return c_max
    
i=[(30, 75), (0, 50), (60, 150)]
print(max_class(i))