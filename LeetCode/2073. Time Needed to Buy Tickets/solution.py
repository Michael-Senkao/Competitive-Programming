class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        n = len(tickets)
        index = 0

        while index <= k:
            ans += min(tickets[index], tickets[k])
            index += 1
        
        tickets[k] -= 1
        
        while index < n:
            ans += min(tickets[index], tickets[k])
            index += 1

        return ans
        
