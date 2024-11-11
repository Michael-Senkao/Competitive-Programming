class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def binarySearch(curr, prev):
            res = curr
            left,right = 0, len(primes) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if primes[mid] < curr:
                    if curr - primes[mid] > prev:
                        res = curr - primes[mid]
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    right = mid - 1
            return res
        
        max_val = max(nums)
        isPrime = [True]*(max_val + 1)
        isPrime[0] = isPrime[1] = False
        primes = []

        for i in range(2, max_val + 1):
            if isPrime[i]:
                primes.append(i)
                for j in range(i*i, max_val + 1, i):
                    isPrime[j] = False
         
        nums[0] = binarySearch(nums[0], 0)
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                return False
            nums[i] = binarySearch(nums[i], nums[i-1])
        return True