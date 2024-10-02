class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        rank_map = dict()
        rank = 1

        for num in sorted_arr:
            if num not in rank_map:
                rank_map[num] = rank
                rank += 1

        arr = [rank_map[num] for num in arr]
        return arr