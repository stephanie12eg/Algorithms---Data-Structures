def solution(S):
    # write your code in Python 3.8.10
    pass
    stack = []
    
    for char in S:
        if char == '(':
            stack.append(char)
        
        elif char == ')':
            if len(stack) == 0:
                return 0
            else:
                stack.pop()
    
    if len(stack) == 0:
        return 1
    else:
        return 0