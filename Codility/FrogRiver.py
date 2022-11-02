# solution 1, failed perfomance test 54% score
def solution(X, A):
    # write your code in Python 3.8.10
    pass
    array = X*[None]
    index = 0

    for i in range(len(A)):
        if A[i] <=X and A[i] not in array:
            array[index] = A[i]
            index +=1
        if None not in array:
            return i 
    
    if None in array: 
        return -1 

# solution 2, failed perfomance test 54% score   
def solution(X, A):
    # write your code in Python 3.8.10
    pass
    array = X*[None]

    for i in range(len(A)):
        if A[i] <=X and i not in array:
            array[A[i]-1] = i
        if None not in array:
            return max(array)
    
    
    return -1 
# solution 3 100%
def solution(X, A):
    # write your code in Python 3.8.10
    pass
    array = X*[-1]

    for i in range(len(A)):
        if A[i] <=X and array[A[i]-1] == -1:
            array[A[i]-1] = i
    m = 0 
    for i in range(len(array)):
        if array[i] == -1:
            return -1 
        m =max(m,array[i])

    return m