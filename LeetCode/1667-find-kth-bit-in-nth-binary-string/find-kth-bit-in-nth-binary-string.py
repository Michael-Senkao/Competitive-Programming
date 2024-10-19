class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s_n = '0'
        def invert(s_n):
            s_n_l = ['0' if ch == '1' else '1' for ch in s_n]
            return ''.join(reversed(s_n_l))

        while k > len(s_n)*2+1:
            s_n = s_n + '1' + invert(s_n)
        if k <= len(s_n):
            return s_n[k-1]
        if k == len(s_n)+1:
            return "1"
        else:
            x = s_n[-(k-(len(s_n)+1))]
            return '1' if x == '0' else '0'