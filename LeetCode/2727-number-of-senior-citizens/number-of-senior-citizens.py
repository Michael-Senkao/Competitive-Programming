class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for person in details:
            ans += (int(person[11:13]) > 60)
        return ans