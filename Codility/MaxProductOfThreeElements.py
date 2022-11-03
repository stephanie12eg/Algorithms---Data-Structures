def solution(A):
    # write your code in Python 3.8.10
    pass
    
    m=0
    
    A.sort()
    m = max(A[-3]*A[-2]*A[-1], A[0]*A[1]*A[-1])

    return m