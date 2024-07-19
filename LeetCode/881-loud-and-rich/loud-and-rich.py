class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        ans = [i for i in range(n)]
        adj = defaultdict(list)
        indegree = [0 for _ in range(n)]

        for a,b in richer:
            adj[a].append(b)
            indegree[b] += 1

        q = deque()
        for person in range(n):
            if indegree[person] == 0:
                q.append(person)

        while q:
            curr = q.popleft()
            parent = ans[curr]
            for nei in adj[curr]:
                child = ans[nei]
                if quiet[parent] < quiet[child]:
                    ans[nei] = parent
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return ans