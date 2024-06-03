class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        brackets = {'{':'}', '[':']', '(': ')'}
        stack = []
        
        for bracket in x:
            if bracket in brackets.keys():
                stack.append(bracket)
            elif stack and brackets[stack[-1]] == bracket:
                stack.pop()
            else:
                return False
                
        return not stack
