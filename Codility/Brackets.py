# solution 1
def solution(S):
    
    brackets = {"[": "]", "(": ")", "{": "}"}
    stack = []
    for char in S:
        if char in brackets.keys():
            stack.append(brackets[char])
        elif char in brackets.values():
            if len(stack) == 0 or stack.pop() != char:
                return 0
    return 1 if len(stack) == 0 else 0

# solution 2
def solution(S):
    # write your code in Python 3.6
    
    B = []
    
    for char in S: 
        if char == '{' or char == '[' or char == '(':
            B.insert( len(B), char) # inserting value according to index
    
        # note: check if the stack is empty or not (be careful)
        if len(B) == 0:
            return 0
        elif char == ')':
            pop = B.pop( len(B)-1 )
            if pop != '(':
                return 0
        elif char == ']':
            pop = B.pop( len(B)-1 )
            if pop != '[':
                return 0
        elif char == '}':
            pop = B.pop( len(B)-1 )
            if pop != '{':
                return 0
    
    # note: check if the stack is empty or not (be careful)
    if len(B)==0:
        return 1
    else:
        return 0

# solution 3 (removing index specification)
def solution(S):
    # write your code in Python 3.8.10
    pass
    B = []
    
    for char in S: 
        if char == '{' or char == '[' or char == '(':
            B.append(char) 
        if len(B) == 0:
            return 0

        elif char == ')':
            pop = B.pop()
            if pop != '(':
                return 0
        elif char == ']':
            pop = B.pop()
            if pop != '[':
                return 0
        elif char == '}':
            pop = B.pop()
            if pop != '{':
                return 0
    
    if len(B)==0:
        return 1
    else:
        return 0
