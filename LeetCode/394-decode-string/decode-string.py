class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []

        for ch in s:
            if ch == ']':
                k = []
                curr_word = []
                while stack[-1].isalpha():
                    curr_word.append(stack.pop())

                stack.pop()
                while stack and stack[-1].isnumeric():
                    k.append(stack.pop())
                
                curr_word.reverse()
                curr_word = "".join(curr_word)
                k.reverse()
                k = "".join(k)
                stack.append(int(k)*curr_word)
            else:
                stack.append(ch)
     
        return ''.join(stack)
             
     