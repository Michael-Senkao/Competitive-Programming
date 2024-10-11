class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times) 

        indices = [i for i in range(n)]

        indices.sort(key=lambda i: times[i][0])
        
        free = [i for i in range(n)]
        taken = []
        heapq.heapify(free)
        heapq.heapify(taken)

        for i in indices:
            start,end = times[i]
            while taken and taken[0][0] <= start:
                _, index = heapq.heappop(taken)
                heapq.heappush(free, index)
            if i == targetFriend:
                return free[0]
            index = heapq.heappop(free)
            heapq.heappush(taken, (end, index))

        return -1