class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canCarry(maxCapacity):
            
            count = 1
            current = 0
            for weight in weights:
                if weight > maxCapacity:
                    return False
                current += weight
                if current > maxCapacity:
                    count += 1
                    current = weight
                
            return count <= days
        
        n = len(weights)
        total = sum(weights)
        l,r = 1, total

        while l < r:
            mid = l + (r - l)//2
            if canCarry(mid):
                r = mid
            else:
                l = mid + 1

        return l

