def solution(A, K):
    # write your code in Python 3.8.10
    pass
    if K == len(A):
        return A
    
  
    rotatedArray= [None]*len(A)

    for i in range (len(A)): 
        rotatedArray[(i+K)%len(A)]= A[i] #modulus ensures that when the index exceeds the length of the array, the index goes back to the start of the array  
    
    return rotatedArray