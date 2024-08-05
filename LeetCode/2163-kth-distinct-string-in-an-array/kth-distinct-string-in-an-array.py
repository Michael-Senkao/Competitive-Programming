class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        string_freq = Counter(arr)

        for string in arr:
            if string_freq[string] == 1:
                k -= 1
            if k == 0:
                return string
        return ""