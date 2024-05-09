class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n = len(happiness)
        happiness.sort(reverse = True) # Sort the array in descending order
        current_index = 0
        ans = 0

        # From the first k childern, subtract the current index (i.e., the number of times it will be subtracted) from their happiness level
        # If the value is negative, add 0 to answer, else add the value to answer
        while k > 0:
            ans += max(0, happiness[current_index] - current_index)
            current_index += 1
            k -= 1
        
        return ans
