class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        stack = []
        score = None
        for i in range(n):
            
            if s[i] == '(':
                stack.append('(')
                continue
            elif stack[-1] == '(':
                score = 1
                stack.pop()
            else:
                score = stack[-1] * 2
                stack.pop()
                stack.pop()
            if not stack or stack[-1] == '(':
                    stack.append(score)
            else:
                stack[-1] += score
                
        return stack[-1]
