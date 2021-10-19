# Problem link: https://leetcode.com/problems/merge-intervals/
# Tags: Facebook, Google, Microsoft, Apple

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        len_intervals = len(intervals)
        if len_intervals == 1:
            return intervals
            
        merged_arr = []
        idx = 0
        while idx in range(len_intervals-1):
            if intervals[idx][0] <= intervals[idx+1][0] and intervals[idx+1][0] <= intervals[idx][1]:
                merged_arr.append([intervals[idx][0], max(intervals[idx][1], intervals[idx+1][1])])
                idx += 1
            else:
                merged_arr.append(intervals[idx])
            idx += 1
        
        if merged_arr[-1][1] != intervals[-1][1]:
            merged_arr.append(intervals[-1])
        return merged_arr