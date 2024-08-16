from sortedcontainers import SortedSet
class SmallestInfiniteSet:

    def __init__(self):
        self.next = 1
        self.integers_set = SortedSet()
        

    def popSmallest(self) -> int:
        if self.integers_set:
            return self.integers_set.pop(0)
        val = self.next
        self.next += 1
        return val
        

    def addBack(self, num: int) -> None:
        if num < self.next:
            self.integers_set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)