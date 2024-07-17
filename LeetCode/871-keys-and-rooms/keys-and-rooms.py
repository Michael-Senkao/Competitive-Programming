class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        q = deque([0])
        visited = set([0])
    
        while q:
            curr = q.popleft()
            for room in rooms[curr]:
                if room not in visited:
                    visited.add(room)
                    q.append(room)

        return len(visited) == len(rooms)