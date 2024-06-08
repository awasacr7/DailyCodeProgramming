def encoding(a):
    if a.startswith('0'):
        return 0
    elif len(a)<=1:
        return 1
    
    result=0
    
    if int(a[:2]) <= 26:
        result += encoding(a[2:])
    
    result += encoding(a[1:])
    return result

print(encoding('12345'))