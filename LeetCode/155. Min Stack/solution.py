class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # Push the current value and the minimum element in the stack at current level onto the stack
        if self.stack:
            self.stack.append((val, min(val, self.stack[-1][1])))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
