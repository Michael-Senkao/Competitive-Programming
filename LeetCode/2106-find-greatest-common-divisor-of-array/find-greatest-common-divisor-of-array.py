class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def euclid_gcd(a,b):
            if b==0:
                return a
            return euclid_gcd(b, a%b)

        return euclid_gcd(max(nums), min(nums))