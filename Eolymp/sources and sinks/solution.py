n = int(input())
adjMatrix = [list(map(int, input().split())) for _ in range(n)]

sinks = [i+1 for i in range(n) if sum(adjMatrix[i]) ==0]
sources = []

for i in range(n):
    for j in range(n):
        if adjMatrix[j][i] == 1:
            break
    else:
        sources.append(i + 1)

print(len(sources), *sources)
print(len(sinks), *sinks)
