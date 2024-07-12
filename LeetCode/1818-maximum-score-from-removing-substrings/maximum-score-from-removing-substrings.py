class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        stack = []
        maxValue=min_value=max_string=min_string = None
        ans = 0

        if x > y:
            max_value,min_value = x,y
            max_string,min_string = "ab","ba"
        else:
            max_value,min_value = y,x
            max_string,min_string = "ba","ab"
        
        for ch in s:
            if ch not in {'a','b'}:
                ans += (min(stack.count('a'), stack.count('b'))*min_value)
                stack = []
            elif stack and stack[-1] + ch == max_string:
                ans += max_value
                stack.pop()
            else:
                stack.append(ch)
        ans += (min(stack.count('a'), stack.count('b'))*min_value)
        return ans

