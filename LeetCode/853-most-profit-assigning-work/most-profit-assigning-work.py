class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        works = list(zip(difficulty, profit))
        n,m = len(profit), len(worker)

        works.sort()
        worker.sort()
        max_profit = 0
        i = 0
        j = 0
        res = 0

        while i < m:
            while j < n and works[j][0] <= worker[i]:
                max_profit = max(max_profit, works[j][1])
                j += 1
            res += max_profit
            i += 1
        return res