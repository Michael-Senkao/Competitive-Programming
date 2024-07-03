from collections import defaultdict
n = int(input())
k = int(input())

graph = defaultdict(list)
for i in range(k):
    operation, *operands = input().split()
    if operation == '1':
        graph[operands[0]].append(int(operands[1]))
        graph[operands[1]].append(int(operands[0]))
    else:
        if operands[0] in graph:
            print(*graph[operands[0]])
        
