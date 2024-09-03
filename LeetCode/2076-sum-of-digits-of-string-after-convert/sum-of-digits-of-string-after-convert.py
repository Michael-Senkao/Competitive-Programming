class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def transform(num_str):
            sum_of_digit = 0
            for ch in num_str:
                sum_of_digit += int(ch)
            return str(sum_of_digit)

        num_str = []

        for ch in s:
            num_str.append(str(ord(ch) - ord('a') + 1))

        num_str = "".join(num_str)
        while k > 0:
            num_str = transform(num_str)
            k -= 1
       
        return int(num_str)