class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        adj = defaultdict(list)
        indegree = defaultdict(int)
        finish_time = [0 for _ in range(n)]

        for prev,next_ in relations:
            adj[prev].append(next_)
            indegree[next_] += 1

        q = deque()
        for i in range(1,n+1):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
    
            curr = q.popleft()
            finish_time[curr-1] += time[curr-1]
            for nei in adj[curr]:
                if finish_time[nei - 1] == 0:
                    finish_time[nei - 1] = finish_time[curr-1]
                else:
                    finish_time[nei - 1] = max(finish_time[nei - 1], finish_time[curr - 1])
                
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return max(finish_time)