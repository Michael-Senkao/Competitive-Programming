class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        indegree = [0 for _ in range(numCourses)]
        graph = defaultdict(list)

        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        q = deque()
        pre = defaultdict(set)

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            curr = q.popleft()
            for nei in graph[curr]:
                pre[nei].add(curr)
                pre[nei].update(pre[curr])
                print(pre[nei], pre[curr])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        res = [u in pre[v] for u,v in queries]
      
        return res
                        