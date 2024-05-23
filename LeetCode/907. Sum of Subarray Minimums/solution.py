class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10 ** 9 + 7
        stack = []
        res = 0

        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                j = stack.pop()
                left = j - stack[-1] if stack else j + 1
                right = i - j
                res = (res + arr[j] * left * right) % MOD
            stack.append(i)

        for i in range(len(stack)):
            j = stack[i]
            left = j - stack[i-1] if i > 0 else j + 1
            right = n - j
            res = (res + arr[j] * left * right) % MOD
            
        return res
