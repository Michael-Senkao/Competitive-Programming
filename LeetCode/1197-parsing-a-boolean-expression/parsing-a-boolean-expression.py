class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def evaluate(expr, top, op):
            if op == '|':
                return expr | top
            return expr & top

            
        operators = {'|', '&', '!'}
        operator = []
        stack  = []

        for ch in expression:
            if ch == ',':
                continue
            if ch in operators:
                operator.append(ch)
            elif ch != ')':
                if ch == '(':
                    stack.append(ch)
                else:
                    stack.append(True if ch == 't' else False)
            else:
                expr = stack.pop()
                op = operator.pop()
                if op == '!':
                    expr = not expr
                else:
                    while stack[-1] != '(':
                        expr = evaluate(expr, stack.pop(), op)
                    
                stack.pop()
                stack.append(expr)
                
        return stack[0]
        