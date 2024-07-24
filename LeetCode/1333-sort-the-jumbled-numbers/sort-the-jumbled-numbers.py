class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map_value(num):
            res = ""
            while num > 9:
                rem = num % 10
                res = str(mapping[rem]) + res
                num //= 10
            return int(str(mapping[num]) + res)

        mapped_values = [map_value(num) for num in nums]
        print(mapped_values)
        result = [x[1] for x in sorted(enumerate(nums), key=lambda num: mapped_values[num[0]])]
        # print(result)
        return result