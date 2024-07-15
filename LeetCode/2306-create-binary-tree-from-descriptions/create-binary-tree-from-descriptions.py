# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        def dfs(val):
            parent = TreeNode(val)
            for child in adj[val]:
                if child[1]==1:
                    parent.left = dfs(child[0])
                else:
                    parent.right = dfs(child[0])

            return parent

        def findRoot():
            for parent in adj.keys():
                if parent not in children:
                    return parent


        
        adj = defaultdict(list)
        children = set()
        
        for parent, child, position in descriptions:
            adj[parent].append((child, position))
            children.add(child)

        root = findRoot()
        # print(adj)
        # print(root)
        return dfs(root)