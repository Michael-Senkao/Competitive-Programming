class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Max-heap to store (-gain, current_passes, total_students)
        max_heap = []
        
        for passes, total in classes:
            # Calculate initial gain and push to heap
            gain = (passes + 1) / (total + 1) - passes / total
            heapq.heappush(max_heap, (-gain, passes, total))
        
        # Assign extra students
        while extraStudents > 0:
            # Pop class with max gain
            neg_gain, passes, total = heapq.heappop(max_heap)
            
            # Update class stats
            passes += 1
            total += 1
            
            # Recompute gain and push back to heap
            new_gain = (passes + 1) / (total + 1) - passes / total
            heapq.heappush(max_heap, (-new_gain, passes, total))
            
            extraStudents -= 1
        
        # Compute final average
        total_ratio = 0
        while max_heap:
            _, passes, total = heapq.heappop(max_heap)
            total_ratio += passes / total
        
        return total_ratio / len(classes)
