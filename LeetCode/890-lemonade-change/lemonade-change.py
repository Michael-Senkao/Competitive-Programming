class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 10:
                if change[5] == 0:
                    return False
                change[5] -= 1
            elif bill == 20:
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                elif change[10] > 0 or change[5] < 3:
                    return False
                else:
                    change[5] -= 3
            change[bill] += 1
        return True

