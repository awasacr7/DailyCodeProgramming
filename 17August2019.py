def largestSumNonAdj(a):
    if not a:
        return 0
    
    return max(largestSumNonAdj(a[1:]),a[0]+largestSumNonAdj(a[2:]))

print(largestSumNonAdj([2,4,6,8]))