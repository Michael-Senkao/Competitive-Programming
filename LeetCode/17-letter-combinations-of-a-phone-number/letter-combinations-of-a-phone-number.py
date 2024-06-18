class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        n = len(digits)
        keys = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", 
        "7":"pqrs", "8": "tuv", "9":"wxyz"
        }

        def backtrack(index, current):
            if index >= n:
                res.append(current)
                return
            for letter in keys[digits[index]]:
                backtrack(index + 1, current + letter)
        if digits:
            backtrack(0, "")
        return res
        