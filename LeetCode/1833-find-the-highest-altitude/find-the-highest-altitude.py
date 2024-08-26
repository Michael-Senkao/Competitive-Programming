class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        running_sum = 0
        max_gain = 0

        for val in gain:
            running_sum += val
            max_gain = max(max_gain, running_sum)

        return max_gain
        