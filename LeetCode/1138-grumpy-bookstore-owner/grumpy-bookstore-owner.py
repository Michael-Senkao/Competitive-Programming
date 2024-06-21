class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n=len(customers)
        
        satisfied = 0
        window_sum = 0
        max_unsatisfied = 0
        left,right = 0,0

        while right < n:
            window_sum += customers[right] if grumpy[right]==1 else 0
            satisfied += customers[right] if grumpy[right]==0 else 0

            while right - left >= minutes:
                if grumpy[left]==1:
                    window_sum -= customers[left]
                left += 1
            max_unsatisfied = max(max_unsatisfied, window_sum)
            right += 1
        
        return satisfied + max_unsatisfied