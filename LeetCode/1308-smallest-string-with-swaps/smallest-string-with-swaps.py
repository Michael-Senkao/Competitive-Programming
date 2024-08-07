# class UnionFind:
#     def __init__(self, n):
#         self.parent = [i for i in range(n)]
#         self.rank = [1 for _ in range(n)]

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def bfs(index):
            q = deque([index])
            visited.add(index)
            string = ""
            indexes = []
            while q:
                curr = q.popleft()
                indexes.append(curr)
                string += s[curr]
                for nei in adj[curr]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            
            string = sorted(string)
            # print(string, indexes)
            j = 0
            for i in sorted(indexes):
                result[i] = string[j]
                j += 1
            
        
        adj = defaultdict(list)

        for u,v in pairs:
            adj[u].append(v)
            adj[v].append(u)
        
        n = len(s)
        visited = set()
        
        result = [""]*n
        for i in range(n):
            if i not in visited:
                bfs(i)
        # print(result)
        return "".join(result)