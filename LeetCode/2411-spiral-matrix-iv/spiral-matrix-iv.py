# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        def move(r,c, dir):
            nonlocal curr
            if dir=='r':
                while curr and c < n and ans[r][c] == -1:
                    ans[r][c] = curr.val
                    curr = curr.next
                    c += 1
            
                r += 1
                c -= 1
            elif dir=='l':
                while curr and c >= 0 and ans[r][c] == -1:
                    ans[r][c] = curr.val
                    curr = curr.next
                    c -= 1
                r -= 1
                c += 1
            elif dir=='d':
                while curr and r < m and ans[r][c] == -1:
                    ans[r][c] = curr.val
                    curr = curr.next
                    r += 1
                r -= 1
                c -= 1
            else:
                while curr and r >= 0 and ans[r][c] == -1:
                    ans[r][c] = curr.val
                    curr = curr.next
                    r -= 1

                r += 1
                c += 1

            return (r,c)
        
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        curr = head
        r = c = 0

        while curr:
            # print(r,c)
            if curr:
                r,c = move(r,c, 'r')
            # print(r,c)
            if curr:
                r,c = move(r,c, 'd')
            # print(r,c)
            if curr:
                r,c = move(r,c, 'l')
            # print(r,c)
            if curr:
                r,c = move(r,c, 'u')
            # print(r,c)
        

        return ans
        