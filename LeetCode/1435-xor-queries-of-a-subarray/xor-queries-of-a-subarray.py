class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0]
        ans = []

        for num in arr:
            prefix.append(prefix[-1] ^ num)
       
        print(prefix)
        for q in queries:
            ans.append(prefix[q[1] + 1] ^ prefix[q[0]])
            

        return ans