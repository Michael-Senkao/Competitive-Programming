class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []

        for ch in s:
            if not stack or ch in ("(", "{", "["): 
                stack.append(ch)
            elif stack[-1]=="[" and ch=="]" or stack[-1]=="(" and ch==")" or stack[-1]=="{" and ch=="}":
                stack.pop()
            else:
                return False
        
        return not stack
