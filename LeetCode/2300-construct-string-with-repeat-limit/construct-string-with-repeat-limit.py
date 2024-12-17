
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = [0]*26
        res = []
        for char in s:
            count[ord(char)-97]+=1
        max_index = 25
        while max_index >=0:
            while max_index >=0 and not count[max_index]:
                max_index-=1
            if max_index < 0:
                return ''.join(res)

            repeat = min(repeatLimit,count[max_index])
            count[max_index]-=repeat
            for _ in range(repeat):
                res.append(chr(max_index+97))
            if count[max_index] == 0:
                continue
            
            next_max = max_index-1
            while next_max >=0 and not count[next_max]:
                next_max-=1
            if next_max < 0:
                return ''.join(res)
            res.append(chr(next_max+97))
            count[next_max]-=1

        return ''.join(res)