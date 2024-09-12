class RecentCounter:

    def __init__(self):
        self.calls = []
        heapq.heapify(self.calls)
        

    def ping(self, t: int) -> int:
        while self.calls and ((t - self.calls[0]) > 3000):
            heapq.heappop(self.calls)
        heapq.heappush(self.calls, t)

        return len(self.calls)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)