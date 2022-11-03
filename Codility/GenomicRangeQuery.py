def solution(S, P, Q):
    # write your code in Python 3.8.10
    pass
    R = []
    for (c, d) in zip(P,Q): # ziping start and end ranges 
        if 'A' in S[c:d+1]: # slicing given S at starting point P and Q with Q included 
            R.append(1)
        elif 'C' in S[c:d+1]:
            R.append(2)
        elif 'G' in S[c:d+1]:
            R.append(3)
        else:
            R.append(4)
            
    return R