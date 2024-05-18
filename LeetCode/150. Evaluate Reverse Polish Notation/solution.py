class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        op = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x,y: x*y, '/': lambda x,y: int(x/y)}

        for token in tokens:
            if token in ('+', '-', '/', '*'):
                y = stack[-1]
                stack.pop()
                x = stack[-1]
                stack.pop()

                stack.append(op[token](x,y))
            else:
                stack.append(int(token))

        return stack[-1]
