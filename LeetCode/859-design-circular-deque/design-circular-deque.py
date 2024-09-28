class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [0 for _ in range(k)]
        self.front = self.back = -1
        

    def insertFront(self, value: int) -> bool:
        if self.front == -1:
            self.q[0] = value
            self.front = self.back = 0
            return True

        index = self.front - 1 if self.front > 0 else len(self.q) - 1
        if index == self.back:
            return False
        self.q[index] = value
        self.front = index

        return True
        

    def insertLast(self, value: int) -> bool:
        if self.front == -1:
            self.q[0] = value
            self.front = self.back = 0
            return True

        index = self.back + 1 if self.back < len(self.q) - 1 else 0
        if index == self.front:
            return False
        self.q[index] = value
        self.back = index

        return True
        

    def deleteFront(self) -> bool:
        if self.front == -1:
            return False
        if self.front == self.back:
            self.front = self.back = -1
        else:
            self.front = self.front + 1 if self.front < len(self.q) - 1 else 0
        return True
        

    def deleteLast(self) -> bool:
        if self.front == -1:
            return False
        if self.front == self.back:
            self.front = self.back = -1
        else:
            self.back = self.back - 1 if self.back > 0 else len(self.q) - 1
        return True
        

    def getFront(self) -> int:
        if self.front == -1:
            return -1
        return self.q[self.front]
        

    def getRear(self) -> int:
        if self.front == -1:
            return -1
        return self.q[self.back]
        

    def isEmpty(self) -> bool:
        return self.front == -1
        

    def isFull(self) -> bool:
        if self.front < self.back:
            return self.back - self.front + 1 == len(self.q)
        return self.back + 1 + len(self.q) - self.front == len(self.q) 

        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()