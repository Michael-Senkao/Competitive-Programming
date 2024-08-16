class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        first_max = second_max = first_min = second_min = None

        if arrays[0][-1] >= arrays[1][-1]:
            first_max, second_max = 0,1
        else:
            first_max, second_max = 1,0

        if arrays[0][0] <= arrays[1][0]:
            first_min, second_min = 0,1
        else:
            first_min, second_min = 1,0

        for i in range(2, n):
            if arrays[i][0] < arrays[first_min][0]:
                second_min = first_min
                first_min = i
            elif arrays[i][0] < arrays[second_min][0]:
                second_min = i

            if arrays[i][-1] > arrays[first_max][-1]:
                second_max = first_max
                first_max = i
            elif arrays[i][-1] > arrays[second_max][-1]:
                second_max = i
        if first_max != first_min:
            return abs(arrays[first_max][-1] - arrays[first_min][0])
        return max(arrays[first_max][-1] - arrays[second_min][0], arrays[second_max][-1] - arrays[first_min][0])