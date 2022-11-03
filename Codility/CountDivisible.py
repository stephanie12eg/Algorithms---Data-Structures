# solution 1, doesnt include whether A is divisible by K 
def solution(A, B, K):
    # write your code in Python 3.8.10
    pass
    c= 0
    if (A%K==0):
        c +=1
    c +=(int(B/K)- int(A/K))
    return c

# solution 2, checking whether A is divisible by K is included by doing A-1
def solution(A, B, K):
    return (B // K - (A-1) // K)  