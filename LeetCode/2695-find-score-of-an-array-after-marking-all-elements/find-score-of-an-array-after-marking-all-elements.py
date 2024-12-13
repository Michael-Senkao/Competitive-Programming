class Solution:
    def findScore(self, nums: List[int]) -> int:
        length = len(nums)
        marked = [False]* length
        score = 0
        sortedNums = sorted([(val,index) for index,val in enumerate(nums)])

        for val,index in sortedNums:
            if marked[index]:
                continue
            score +=val
            if index+1 < length:
                marked[index+1] = True
            if index - 1 >= 0:
                marked[index-1] = True
        return score