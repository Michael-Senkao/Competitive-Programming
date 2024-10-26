# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def dfs(node, level):
            if node is None:
                return 0
            height = max(dfs(node.left, level + 1), dfs(node.right, level + 1))
            levels_heap[level].append((-height, node.val))
            levels[node.val] = level
            return height + 1
        
        levels_heap = defaultdict(list)
        levels = {}
        result = []


        dfs(root, 0)
        for key in levels_heap.keys():
            heapify(levels_heap[key])
        
        for q in queries:
            level = levels[q]
            if levels_heap[level][0][1] != q:
                result.append(-levels_heap[level][0][0] + level)
            elif len(levels_heap[level]) == 1:
                result.append(level - 1)
            else:
                node_tuple = heappop(levels_heap[level])
                result.append(-levels_heap[level][0][0] + level)
                heappush(levels_heap[level], node_tuple)
        return result