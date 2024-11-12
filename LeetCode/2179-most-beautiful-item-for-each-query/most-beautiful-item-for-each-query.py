class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries = [(num,i) for i,num in enumerate(queries)]
        queries.sort()
        res = [0] * len(queries)
        j = 0
        max_beauty = 0
        for i in range(len(queries)):
            while j < len(items) and items[j][0] <= queries[i][0]:
                max_beauty = max(max_beauty,items[j][1]) 
                j+=1
            res[queries[i][1]] = max_beauty
        return res