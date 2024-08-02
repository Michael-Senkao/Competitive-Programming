class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []
        heapify(self.smallHeap)
        heapify(self.largeHeap)
        

    def addNum(self, num: int) -> None:
        if not self.smallHeap:
            heappush(self.smallHeap, -num)
        elif not self.largeHeap:
            if -self.smallHeap[0] <= num:
                heappush(self.largeHeap, num)
            else:
                heappush(self.largeHeap, -heappop(self.smallHeap))
                heappush(self.smallHeap, -num)
        elif len(self.smallHeap) > len(self.largeHeap):
            if -self.smallHeap[0] <= num:
                heappush(self.largeHeap, num)
            else:
                heappush(self.largeHeap, -heappop(self.smallHeap))
                heappush(self.smallHeap, -num)
        elif len(self.smallHeap) < len(self.largeHeap):
            if self.largeHeap[0] >= num:
                heappush(self.smallHeap, -num)
            else:
                heappush(self.smallHeap, -heappop(self.largeHeap))
                heappush(self.largeHeap, num)
        else:
            if -self.smallHeap[0] <= num:
                heappush(self.largeHeap, num)
            else:
                heappush(self.largeHeap, -heappop(self.smallHeap))
                heappush(self.smallHeap, -num)

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return -self.smallHeap[0]
        elif len(self.smallHeap) < len(self.largeHeap):
            return self.largeHeap[0]
        else:
            return (-self.smallHeap[0] + self.largeHeap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()