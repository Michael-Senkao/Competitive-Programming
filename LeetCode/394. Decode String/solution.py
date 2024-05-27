class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []

        for ch in s:
            if ch == ']':
                k = ''
                curr_word = ''
                while stack and stack[-1].isalpha():
                    curr_word = stack.pop() + curr_word

                stack.pop()
                while stack and stack[-1].isnumeric():
                    k = stack.pop() + k
                stack.append(int(k)*curr_word)
            else:
                stack.append(ch)
     
        return ''.join(stack)
             
     
