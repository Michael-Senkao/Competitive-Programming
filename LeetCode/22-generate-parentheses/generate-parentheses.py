class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(curr, opened_par, closed_par):
            if opened_par == 0:
                curr += ")"*closed_par
                res.append(curr)
            else:
                helper(curr + "(", opened_par - 1, closed_par)
                if closed_par > opened_par:
                    helper(curr + ")", opened_par, closed_par - 1)

        res = []
        helper("(", n-1, n)
        print(res)
        return res