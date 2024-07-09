class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        total_waiting_time = 0
        current_time = 0
        for i in range(n):
            start_time = max(current_time, customers[i][0])
            completion_time = start_time + customers[i][1]
            total_waiting_time += completion_time - customers[i][0]
            current_time = completion_time
        return total_waiting_time / n