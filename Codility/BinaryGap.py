def solution(N):
    
    pass
    
    N= bin(N) [2:]
    gap= 0 
    maxGap= 0 

    for i in N:
        if int(i) == 0:
            gap +=1
        else: 
            maxGap = max(gap, maxGap)
            gap = 0 
    
    return maxGap