def solution(A):
    pass
    carsEast= 0 
    carPairs = 0 
    for i in range(len(A)):
        if A[i] == 0:
            carsEast +=1
        else:
            carPairs +=carsEast
    
    if carPairs> 1000000000:
        return -1
    else:
        return carPairs