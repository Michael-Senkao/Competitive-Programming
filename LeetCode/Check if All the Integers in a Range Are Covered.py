'''
QUESTION:
You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] 
represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. 
Return false otherwise.
'''

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        total_range = set()
        given_range = set()

        # Find all the numbers in the range of all the intervals in 'ranges'
        for interval in ranges:
            for num in range(interval[0], interval[1] + 1):
                total_range.add(num)

        # Find all the numbers in the given range [left, right]
        for num in range(left, right+1):
            given_range.add(num)
        # If given range [left, right] is a subset of the total range, return True otherwise False
        return given_range.issubset(total_range)
