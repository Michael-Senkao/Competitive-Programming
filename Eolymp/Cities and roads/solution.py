n = int(input())
adjacency_matrix = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(i+1, n):
        ans += (adjacency_matrix[i][j] == 1 )

print(ans)
