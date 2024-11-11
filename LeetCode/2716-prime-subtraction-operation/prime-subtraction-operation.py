class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def binarySearch(diff):
            res = diff
            left,right = 0, len(primes) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if primes[mid] < diff:
                    res = primes[mid]
                    left += 1
                else:
                    right = mid - 1
            return res if res != diff else -1
        
        max_val = max(nums)
        isPrime = [True]*(max_val + 1)
        isPrime[0] = isPrime[1] = False
        primes = []

        for i in range(2, max_val + 1):
            if isPrime[i]:
                primes.append(i)
                for j in range(i*i, max_val + 1, i):
                    isPrime[j] = False
        
        diff = binarySearch(nums[0])
        if diff != -1:
            nums[0] -= diff
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                print(nums)
                return False
            max_diff = binarySearch(nums[i] - nums[i-1])
            if max_diff != -1:
                nums[i] -= max_diff
        print(nums)
        return True