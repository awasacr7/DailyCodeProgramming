def solution(btree):
    val, left, right = btree
    
    if left is None and right is None:
        return 1, True , val
    
    lcount , isunil_l , lval = solution(left)
    rcount , isunil_r , rval = solution(right)
    
    isunival = isunil_l and isunil_r and val == lval and val == rval
    count = lcount + rcount + isunival
    return count, isunival , val
    
    
def count_trees(root):
    count, _ = helper(root)
    return count

def helper(root):
    if root is None:
        return 0, True
    
    l_count, l_unival = helper(root.left)
    r_count, r_unival = helper(root.right)
    
    total_count = l_count + r_count
    
    if l_unival and r_unival:
        if root.left is not None and root.value != root.left.value:
            return total_count, False
        if root.right is not None and root.value != root.right.value:
            return total_count, False
        return total_count + 1, True
    return total_count,False

btree=(0, (0, (0, None, None), (0, (0, None, None), (0, None, None))), (1, None, None))
print(solution(btree)[0])