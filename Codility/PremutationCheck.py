def solution(A):
    # write your code in Python 3.8.10
    pass
    A.sort()

    for i in range(len(A)):
        if A[i]-1 != i:
            return 0
    return 1 