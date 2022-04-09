"""Algorithm for computing the prefix average"""
def prefix_average(S):
    # returns a list such that, for all j, A[j] equals average of S[0],...,s[j]
    n = len(S) # get the length of the parameter list
    A = [0] * n # create a new array (same length as input list) with all 0's
    total = 0 # running total, compute prefix sum as S[0] + S[1] + ...
    for j in range(n):
        total += S[j] # update prefix sum to include S[j]
        A[j] = total/(j+1) # computer average based on current sum
    return A
# O(n) #

"""Algorithm to determine if the intersection of three sequences is empty (disjoint)"""
def disjoint(A, B, C):
    ''' Return true if there is no element common to all three lists'''
    for a in A:
        for b in B:
            if a == b:                  # only check C if we found match from A and B
                for c in C:
                    if a == c:          # (and thus a == b == c)
                        return False    # we found a common value
    return True                         # if we reach this, sets are disjoint
# O(n^2) #

"""Algorithm that, given a single sequence S with n elements, tells us whether all elements are distinct from each other"""
def unique(S):
    """Return True if there are no duplicate elements in sequence S"""
    '''By sorting, we can guarantee that any duplicate elements will be placed next to eachother'''
    temp = sorted(S)                # create a sorted copy of S
    for j in range(1, len(temp)):   
        if S[j-1] == S[j]:          # check previous and current element to see if they're the same
            return False            # found duplicate pair
    return True
# O(n log n), sorted runs in O(log n) #


'''Binary Search'''
def binary_search(data, target, low, high):
    """
        Return True if target is found in indicated portion of a Python list
        The search only considers the portion from data[low] to data[high] inclusive
    """
    if low > high:
        return False # interval is empty; no match
    else:
        mid = (low + high) // 2
        if target == data[mid]: # found a match
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid-1)
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid+1, high)
if __name__ == '__main__':
    print(prefix_average([1,3,2,2,3]))
