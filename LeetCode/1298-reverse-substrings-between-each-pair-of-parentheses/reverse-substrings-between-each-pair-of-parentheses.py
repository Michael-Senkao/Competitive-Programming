class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ch in s:
            # print(stack)
            if ch=='(':
                stack.append("")
            elif ch == ')':
                curr = stack.pop()[::-1]
                if stack:
                    stack[-1] += curr
                else:
                    stack.append(curr)
            elif stack:
                stack[-1]+=ch
            else:
                stack.append(ch)
        # print(stack)
        return stack[-1]