# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]

        # open brackets are added to the stack and if they have a corresponding closing bracket, then it will be popped. 
        # If the parentheses are valid then the stack will be empty at the end.

        for char in s: 
            if char =='{' or char=='[' or char=='(':
                stack.insert( len(stack), char) 

            if len(stack) == 0:
                return False
            elif char==')':
                pop=stack.pop( len(stack)-1)
                if pop!='(':
                    return False
            elif char==']':
                pop=stack.pop( len(stack)-1)
                if pop!='[':
                    return False
            elif char=='}':
                pop=stack.pop( len(stack)-1)
                if pop!='{':
                    return False

        if len(stack)!=0:
            return False
        else:
            return True
