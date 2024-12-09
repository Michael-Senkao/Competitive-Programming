class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        special = [1]
        count = 1
        res = []

        for i in range(1, n):
            if nums[i] & 1:
                if nums[i-1] % 2 == 0:
                    count += 1
            elif nums[i-1] & 1:
                count += 1
            special.append(count)

        for start,end in queries:
            if special[end] - special[start] + 1 == end - start + 1:
                res.append(True)
            else:
                res.append(False)
        return res