def solution(A, B):
    # write your code in Python 3.8.10
    pass
    C = []
    eaten = 0
    
    for i in range(len(B)):
        
        # downstream
        if B[i] == 1:
            C.append(A[i])
        else:
            while len(C) != 0:
                if C[-1] > A[i]:
                    eaten +=1
                    break
                elif C[-1] < A[i]:
                    C.pop()
                    eaten +=1
                
        
    return len(A)-eaten
    