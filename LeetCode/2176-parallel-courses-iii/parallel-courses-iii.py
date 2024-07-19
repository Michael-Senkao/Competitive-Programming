class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        adj = defaultdict(list)
        indegree = defaultdict(int)
        ans = [0 for _ in range(n)]
        for prev,next_ in relations:
            adj[prev].append(next_)
            indegree[next_] += 1

        q = deque()
        for i in range(1,n+1):
            if indegree[i] == 0:
                q.append(i)
        # print(adj)
        # print(indegree)
        
        while q:
            # print(q)
            curr = q.popleft()
            ans[curr-1] += time[curr-1]
            for nei in adj[curr]:
                if ans[nei - 1] == 0:
                    ans[nei - 1] = ans[curr-1]
                else:
                    ans[nei - 1] = max(ans[nei - 1], ans[curr - 1])
                
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        # print(ans)
        return max(ans)