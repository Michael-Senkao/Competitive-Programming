class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        costs = {node: float("inf") for node in range(1, n+1)}
        indegree = {node: 0 for node in range(1, n+1)}

        for u,v,w in times:
            graph[u].append((v,w))
            indegree[v] += 1

        visited = set()
        q = [(0, k)]
        heapify(q)
        # visited.add(k)
        costs[k] = 0
        

        while q:
            # print(q)
            curr_cost, current_node = heappop(q)
            if current_node in visited:
                continue
            costs[current_node] = curr_cost
            visited.add(current_node) 
            for neighbor, cost in graph[current_node]:
                heappush(q, (curr_cost + cost, neighbor))

        if len(visited) != n:
            return -1
        return max(costs.values())