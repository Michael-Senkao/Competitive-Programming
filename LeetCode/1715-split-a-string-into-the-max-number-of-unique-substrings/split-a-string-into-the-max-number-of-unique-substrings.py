class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def helper(index, curr, result: set):
            if index == len(s):
                if curr and curr not in result:
                    return len(result) + 1
                return len(result)

            include = helper(index + 1, curr + s[index], result)
            if not curr or curr in result:
                return include

            result.add(curr)
            exclude = helper(index + 1, s[index], result)
            result.remove(curr)
            return max(include, exclude)

        return helper(1, s[0], set())
                
        