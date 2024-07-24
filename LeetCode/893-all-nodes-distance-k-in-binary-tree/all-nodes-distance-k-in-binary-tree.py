# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)

        graph = defaultdict(list)
        result = []
        dfs(root)

        q = deque([(target.val, 0)])
        visited = set()
        visited.add(target.val)

        while q:
            node, distance = q.popleft()
            if distance == k:
                result.append(node)
            else:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        q.append((neighbor, distance + 1))
                        visited.add(neighbor)


        return result