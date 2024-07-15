from collections import defaultdict, deque

def solve(n):
    def bfs(node):
        visited.add(node)
        for child in adj[node]:
            if child not in visited:
                if child not in color:
                    color[child] = -1*color[node]
                elif color[child] == color[node]:
                    return False
        return True


    edges = int(input())
    adj = defaultdict(list)
    for _ in range(edges):
        u,v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    visited = set()
    color = {1: 1}
    for node in range(1, n+1):
        if not bfs(node):
            return "NOT BICOLOURABLE."
    return "BICOLOURABLE."

while True:
    n = int(input())
    if n==0:
        break
    
    print(solve(n))
