class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.capacity = maxSize
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.capacity:
            self.stack.append(x)
        

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1
        

    def increment(self, k: int, val: int) -> None:
        m = min(len(self.stack), k)
        for i in range(m):
            self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)