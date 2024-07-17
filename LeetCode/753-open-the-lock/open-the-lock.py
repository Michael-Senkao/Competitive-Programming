class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def children(curr_lock):
            result = []
            for i in range(4):
                x = curr_lock[i]
                forward = (int(x) + 1) % 10
                backward = (int(x) - 1 + 10) % 10
                result.append(curr_lock[:i] + str(forward) + curr_lock[i+1:])
                result.append(curr_lock[:i] + str(backward) + curr_lock[i+1:])
            return result



        q = deque()
        visited = set(deadends)
        if "0000" in visited:
            return -1

        q.append(("0000", 0))
        while q:
            curr_lock, turns = q.popleft()
            if curr_lock == target:
                return turns
            
            for child in children(curr_lock):
                if child not in visited:
                    q.append((child, turns + 1))
                    visited.add(child)

        return -1