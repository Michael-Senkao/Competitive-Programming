class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0

        for p in s:
            if p == '(':
                stack.append('(')
            elif stack and stack[-1] == '(':
                stack.pop()
            else:
                res += 1
        
        res += len(stack)
        return res
