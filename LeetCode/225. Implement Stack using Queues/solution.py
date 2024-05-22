class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        n = len(self.queue)
        while n > 1:
            self.queue.append(self.queue.popleft())
            n -= 1
        
        num = self.queue.popleft()
        return num

        

    def top(self) -> int:
        n = len(self.queue)
        while n > 1:
            self.queue.append(self.queue.popleft())
            n -= 1
        
        num = self.queue.popleft()
        self.queue.append(num)

        return num

    def empty(self) -> bool:
        return len(self.queue) == 0
