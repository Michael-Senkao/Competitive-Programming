class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        range_sum = [0]*(1001)
        
        for trip in trips:
            range_sum[trip[1]] += trip[0]
            range_sum[trip[2]] -= trip[0]

        if range_sum[0] > capacity:
            return False

        for i in range(1, 1001):
            range_sum[i] += range_sum[i-1]
            if range_sum[i] > capacity:
                return False
                    
        return True
