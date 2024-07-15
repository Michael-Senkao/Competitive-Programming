# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        def makeNode(parent, child, position):
            if position == 1:
                parent.left = child
            else:
                parent.right = child
            return parent

        adj = defaultdict(TreeNode)
        children = set()
        
        for parent, child, position in descriptions:
            if parent in adj and child in adj:
                adj[parent] = makeNode(adj[parent], adj[child], position)
            elif parent in adj:
                childNode = TreeNode(child) 
                adj[parent] = makeNode(adj[parent], childNode, position)
                adj[child] = childNode
            elif child in adj:
                parNode = TreeNode(parent)
                adj[parent] = makeNode(parNode, adj[child], position) 
            else:
                childNode = TreeNode(child)
                adj[parent] = makeNode(TreeNode(parent), childNode, position)
                adj[child] = childNode

            children.add(child)


        for val,node in adj.items():
            if val not in children:
                return node
    