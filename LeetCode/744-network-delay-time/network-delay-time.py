class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        costs = {node: float("inf") for node in range(1, n+1)}
        indegree = {node: 0 for node in range(1, n+1)}

        for u,v,w in times:
            graph[u].append((v,w))
            indegree[v] += 1

        visited = set()
        q = deque([k])
        visited.add(k)
        costs[k] = 0
        

        while q:
            current_node = q.popleft()
            for neighbor, cost in graph[current_node]:
                if neighbor in visited and costs[current_node] + cost < costs[neighbor]:
                    costs[neighbor] =  costs[current_node] + cost
                    q.append(neighbor)
                elif neighbor not in visited:
                    costs[neighbor] = costs[current_node] + cost
                    q.append(neighbor)
                    visited.add(neighbor)

        # print(costs)
        # print(visited)
        res = 0
        for c in costs.values():
            if c == float("inf"):
                return -1
            res = max(res, c)
        return res