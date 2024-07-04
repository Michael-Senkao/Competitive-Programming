"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(e_id):
            sum = 0
            for subordinate in graph[e_id][1:]:
                sum += dfs(subordinate)
            return sum + graph[e_id][0]


        graph = {}
        for employee in employees:
            graph[employee.id] = [employee.importance] + employee.subordinates

        return dfs(id)