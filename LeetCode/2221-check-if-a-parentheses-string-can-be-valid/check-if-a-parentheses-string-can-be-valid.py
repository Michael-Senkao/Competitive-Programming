class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n & 1:
            return False

        locked_stack = []
        unlocked_stack = []

        for i in range(len(s)):
            if locked[i] == '0':
                unlocked_stack.append(i)
            elif s[i] == '(':
                locked_stack.append(i)
            elif locked_stack:
                locked_stack.pop()
            elif unlocked_stack:
                unlocked_stack.pop()
            else:
                return False
                
        i = j = 0

        while i < len(unlocked_stack) and j < len(locked_stack):
            if unlocked_stack[i] > locked_stack[j]:
                j += 1
            i += 1
        return j == len(locked_stack)
            
        