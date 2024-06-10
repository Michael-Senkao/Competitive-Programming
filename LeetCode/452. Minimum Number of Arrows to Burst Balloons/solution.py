class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        res = n
        
        points.sort()
        previous_end = points[0][1]
        

        for i in range(1, n):
            if points[i][0] <= previous_end:
                res -= 1
                previous_end = min(previous_end, points[i][1])
            else:
                previous_end = points[i][1]

        return res
