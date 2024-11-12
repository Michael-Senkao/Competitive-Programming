class Solution:
    def search(self,target,max_beauties):
        left = 0
        right = len(max_beauties)-1
        res = 0
        while left <= right:
            mid = left + (right-left)//2
            if max_beauties[mid][0] <= target:
                res = max_beauties[mid][1]
                left = mid+1
            else:
                right = mid-1
        return res
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        max_beauties = []
        max_beauty = items[0][1]
        for i in range(1,len(items)):
            if items[i][0] != items[i-1][0]:
                max_beauties.append((items[i-1][0],max_beauty))
            max_beauty = max(max_beauty,items[i][1])
        max_beauties.append((items[-1][0],max_beauty))
        return [self.search(i,max_beauties) for i in queries]