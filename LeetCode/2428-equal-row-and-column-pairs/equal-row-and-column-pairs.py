class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        rows_dict = defaultdict(int)

        for row in grid:
            rows_dict[tuple(row)] += 1

        for c in range(n):
            col = []
            for r in range(n):
                col.append(grid[r][c])
            res += rows_dict[tuple(col)]
        return res