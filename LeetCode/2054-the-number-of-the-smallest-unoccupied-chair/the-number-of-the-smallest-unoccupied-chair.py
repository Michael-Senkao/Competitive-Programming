class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Get the number of time intervals
        n = len(times) 

        # Create a list of indices for the time intervals
        indices = [i for i in range(n)]

        # Sort the indices based on the start time of each interval
        indices.sort(key=lambda i: times[i][0])

        # Initialize a heap for free resources and another for taken resources
        free = [i for i in range(n)]    # All resources are initially free
        taken = []                      # No resources are taken initially
        heapq.heapify(free)             # Turn the list into a heap
        heapq.heapify(taken)            # Turn the empty list into a heap

        # Iterate over the sorted indices based on start times
        for i in indices:
            start, end = times[i]  # Get the start and end times of the current interval

            # Free up resources that have finished before the current start time
            while taken and taken[0][0] <= start:
                _, index = heapq.heappop(taken)  # Remove the resource from the taken heap
                heapq.heappush(free, index)      # Add the freed resource back to the free heap

            # If this is the target friend, return the first available resource
            if i == targetFriend:
                return free[0]  # Return the first available resource (heap root)

            # Allocate a free resource for the current interval
            index = heapq.heappop(free)            # Get the next free resource
            heapq.heappush(taken, (end, index))    # Mark the resource as taken until 'end' time

        # If the target friend isn't found, return -1
        return -1
