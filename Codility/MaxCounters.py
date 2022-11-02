# solution 1 64%
def solution(N, A):
    # write your code in Python 3.8.10
    pass

    array = [0]*N

    for i in range(len(A)):
        if A[i] == N+1:
            array = [max(array)]*N
        else: 
            array[A[i]-1] +=1
    
    return array

# solution 2 77%
def solution(N, A):
    # write your code in Python 3.8.10
    pass
    m = 0
    array = [0]*N

    for i in range(len(A)):
        if A[i] == N+1:
            array = [m]*N
        else: 
            array[A[i]-1] +=1
            m = max(m, array[A[i]-1])
    
    return array
