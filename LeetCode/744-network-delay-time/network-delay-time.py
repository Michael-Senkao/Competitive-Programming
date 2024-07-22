class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        costs = {node: float("inf") for node in range(1, n+1)}
        
        for u,v,w in times:
            graph[u].append((v,w))

        visited = set()
        q = [(0, k)]
        heapify(q)
        costs[k] = 0
        

        while q:
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