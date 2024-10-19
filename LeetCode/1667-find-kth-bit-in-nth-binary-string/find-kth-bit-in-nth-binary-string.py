class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s_n = '0'
        def invert(s_n):
            s_n_l = list(s_n)
            for i in range(len(s_n_l)):
                if s_n_l[i]=='0':
                    s_n_l[i]='1'
                else:
                    s_n_l[i]='0'
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