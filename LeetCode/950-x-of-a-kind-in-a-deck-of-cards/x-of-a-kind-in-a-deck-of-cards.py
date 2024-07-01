class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def find_gcd(a,b):
            while b > 0:
                a,b = b,a%b
            return a
        
        freq = list(Counter(deck).values())
        n = len(freq)
        gcd = freq[0]
        i = 1
        while i < n and gcd > 1:
            gcd = find_gcd(gcd, freq[i])
            i += 1

        return gcd > 1