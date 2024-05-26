class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.maxsize = k
        self.size = 0
        self.front, self.rear = -1,-1


    def enQueue(self, value: int) -> bool:
        if self.size < self.maxsize:
            self.rear = (self.rear + 1) % self.maxsize
            self.queue[self.rear] = value
            self.size += 1
            if self.front < 0:
                self.front += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.size > 0:
            self.front = (self.front + 1) % self.maxsize
            self.size -= 1
            return True
        return False

    def Front(self) -> int:
        if self.size > 0:
            return self.queue[self.front]
        return -1

    def Rear(self) -> int:
        if self.size > 0:
            return self.queue[self.rear]
        return -1
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxsize
