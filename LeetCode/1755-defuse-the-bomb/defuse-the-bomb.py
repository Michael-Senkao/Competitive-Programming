class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return n*[0]
        step = k // abs(k)
        start = 1 if step > 0 else n - 2
        stop = n if step > 0 else -1
        res = []
        for i in range(start,stop, step):
            code[i] += code[i - step]
        for i in range(n):
            index = i + k
            if index < 0:
                index += n
                if i == 0:
                    res.append(code[index])
                else:
                    res.append(code[0] - code[i] + code[index])
            elif index >= n:
                index %= n
                if i == n-1:
                    res.append(code[index])
                else:
                    res.append(code[-1] - code[i] + code[index])
            else:
                res.append(code[index] - code[i])
        print(code)
        return res