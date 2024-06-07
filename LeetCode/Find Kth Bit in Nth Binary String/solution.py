class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n==1:
            return "0" # S1 is always 0
        mid = 2**n/2
        if k< mid:
            return str(self.findKthBit(n-1,k)) # K is in lower half
        elif k==mid:
            return "1" # Middle element is always 1
        else:
            return str(1- int(self.findKthBit(n-1,mid-(k-mid)))) # K is in upper half
