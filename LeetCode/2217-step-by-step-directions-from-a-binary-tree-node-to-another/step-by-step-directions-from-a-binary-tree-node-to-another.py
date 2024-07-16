# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def bfs(key):
            q = deque([(root, "")])
            while q:
                node,path = q.popleft()
                if node.val == key:
                    return path
                if node.left:
                    q.append((node.left, path + "L"))
                if node.right:
                    q.append((node.right, path + "R"))
        
        start_path = bfs(startValue)
        dest_path = bfs(destValue)
        
        i = 0
        start_length = len(start_path)
        dest_length = len(dest_path)
        while i < start_length and i < dest_length and  dest_path[i] == start_path[i]:
            i += 1

        result = "U"*(start_length - i) + dest_path[i:]
        # print(start_path)
        # print(dest_path)
        # print(i, result)
        return result