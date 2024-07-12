class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        stack = []
        max_end_char = 'b' if x > y else 'a'
        max_start_char = 'b' if max_end_char == 'a' else 'a'
        max_start,max_end = 0,0
        max_value,min_value = max(x,y),min(x,y)
        total = 0

        for ch in s:
            if ch == max_end_char:
                if max_start > 0:
                    total += max_value
                    max_start -= 1
                else:
                    max_end += 1
            elif ch == max_start_char:
                max_start += 1
            else:
                total += min(max_start, max_end)*min_value
                max_start,max_end = 0,0
                
        total += min(max_start, max_end)*min_value
        return total

