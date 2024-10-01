class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder = defaultdict(int)
        for num in arr:
            num %= k
            need = k - num
            
            if need in remainder:
                remainder[need] -= 1
                if remainder[need] == 0:
                    del remainder[need]
            else:
                num = k if num == 0 else num
                remainder[num] += 1

        return not remainder
        