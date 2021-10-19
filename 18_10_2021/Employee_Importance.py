# Problem link: https://leetcode.com/problems/employee-importance/
# Tags: Google, Amazon


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id             = id
        self.importance     = importance
        self.subordinates   = subordinates

class Solution:
    def __init__(self) -> None:
        self.employee_map = {}
        
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        for employee in employees:
            self.employee_map[employee.id] = employee

        return self.depth_first_search_importance(self.employee_map[id])


    def depth_first_search_importance(self, employee) -> int:
        # Recursion
        if employee == []:
            return

        sum_importance = 0
        for sub in employee.subordinates: # Importance of subordinates
            sum_importance += self.depth_first_search_importance(self.employee_map[sub])
        
        return sum_importance + employee.importance

# Time complexity:
# Building the hash map requires O(n), n = number of employees
# DFS search: O(m) m = the number of subordinates + the employee
# Total: O(m + n)