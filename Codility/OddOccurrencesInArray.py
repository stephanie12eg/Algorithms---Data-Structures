# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# solution 1:
def solution(A):
    # write your code in Python 3.8.10
    pass

    storage= {}

    for i in range (len(A)):
        if A[i] in storage:
            storage[A[i]] +=1
        else:
            storage[A[i]] = 1
    
    for i in storage: 
        if storage[i]%2 !=0:
            return i

#solution 2:
def solution(A):
    # write your code in Python 3.8.10
    pass
    if len(A) == 1:
        return A[0]
    A.sort()
    for i in range (0,len(A)-1,2):
        if A[i]!= A[i+1]:
            return A[i]
    return A[-1]