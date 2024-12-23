# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        swaps = 0

        while q:
            arr = []
            index_of_val = {}
            indices = {}
            n = len(q)
            
            for i in range(n):
                node = q.popleft()
                val = node.val

                indices[i] = val
                index_of_val[val] = i
                arr.append(val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            arr.sort()
            for i in range(n):
                if indices[i] != arr[i]:
                    curr_ind = index_of_val[arr[i]]
                    indices[i],indices[curr_ind] = indices[curr_ind],indices[i]
                    index_of_val[arr[i]] = i
                    index_of_val[indices[curr_ind]] = curr_ind
                    swaps += 1

        return swaps
                    

            