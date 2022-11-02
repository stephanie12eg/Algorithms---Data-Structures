# solution 1 55%, lacks perfomance 
def solution(A):
    # write your code in Python 3.8.10
    pass
    B= []
    for i in A: 
        if i not in B:
            B.append(i)
    
    B.sort()
    if 1 not in B:
        return 1

    for i in range(len(B)-1):
        if B[i]>0 and B[i] != B[i+1]-1:
            return B[i]+1
    
    return B[-1]+1


def solution(A):
    # write your code in Python 3.8.10
    pass
    return min(set(range(1,len(A)+2)).difference(set(A)))

# solution 2, working with lists led to 55% because of low perfomance score 
def solution(A):
    # write your code in Python 3.8.10
    pass
    B= []
    for i in A: 
        if i not in B:
            B.append(i)

    for i in range(1,len(A)+1):
        if i not in B:
            return i
    
    # i had perviously sorted the array and then returned the B[-1]+1 but sorting lowered the perfomance score 
    return len(B)+1


# solution 3, its better to work with dictionaries for better perfomance 
def solution(A):
    # write your code in Python 3.8.10
    pass
    B= {}
    for i in A: 
        if i not in B:
           B[i] = 1

    for i in range(1,len(A)+1):
        if i not in B:
            return i
    
    # i had perviously sorted the array and then returned the B[-1]+1 but sorting lowered the perfomance score 
    return len(B)+1