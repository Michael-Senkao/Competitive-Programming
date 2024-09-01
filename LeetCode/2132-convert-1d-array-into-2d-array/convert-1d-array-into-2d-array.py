class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        result = []
        
        for i in range(0, len(original), n):
            arr = []
            for j in range(i, i + n):
                arr.append(original[j])
            result.append(arr)
        return result