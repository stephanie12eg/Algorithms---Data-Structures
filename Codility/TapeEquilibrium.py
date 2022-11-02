# solution 1
def solution(A):
    # write your code in Python 3.8.10
    pass
    total = sum(A) 

    minDiff = None # solution ingoring the constraints
    ls = 0
    for i in range(len(A) - 1):
        ls += A[i]
        rs = total - ls 
        diff = abs(ls - rs)
        if minDiff == None: 
            minDiff= diff
        minDiff = min(minDiff, diff)

    return minDiff

# solution 2
def solution(A):
    total = sum(A) 

    min_diff = 9999 
    ls = 0
    for i in range(len(A) - 1):
        ls += A[i]
        rs = total - ls 
        diff = abs(ls - rs)
        min_diff = min(min_diff, diff)