class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if ast >= 0:
                stack.append(ast)
            else:
                while stack and stack[-1] >= 0:
                    if stack[-1] < abs(ast):
                        stack.pop()
                    elif stack[-1] > abs(ast):
                        break
                    else:
                        stack.pop()
                        break
                else:
                    stack.append(ast)

        return stack
