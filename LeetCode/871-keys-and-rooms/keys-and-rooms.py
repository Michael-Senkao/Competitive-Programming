class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        n = len(rooms)
        visited = set()
        visited.add(0)
        q = deque()
        q.append(0)

        while q:
            current = q.popleft()
            for key in rooms[current]:
                if key not in visited:
                    q.append(key)
                    visited.add(key)

        return len(visited) == n