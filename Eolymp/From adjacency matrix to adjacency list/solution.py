from collections import defaultdict

n = int(input())

adjMatrix = [list(map(int, input().split())) for _ in range(n)]

adjList = defaultdict(list)

for i in range(n):
    for j in range(n):
        if adjMatrix[i][j] == 1:
            adjList[i+1].append(j+1)

for vertex,adj in adjList.items():
    print(vertex, *adj)
