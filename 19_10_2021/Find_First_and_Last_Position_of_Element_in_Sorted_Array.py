class Solution:
    def __init__(self) -> None:
        self.nums       = []
        self.target     = 0
        self.len_nums   = 0

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums       = nums
        self.target     = target
        self.len_nums   = len(self.nums)
        if self.len_nums == 0:
            return [-1, -1]
        
        # Starting boundary:
        start_left  = 0
        start_right = self.len_nums - 1

        while start_left < start_right:
            start_mid = (start_left + start_right)//2
            if self.start_boundary_condition(start_mid):
                start_right = start_mid
            else:
                start_left  = start_mid + 1

        # Ending boundary:
        end_left    = start_left
        end_right   = self.len_nums

        while end_left < end_right:
            end_mid = (end_left + end_right)//2
            if self.end_boundary_condition(end_mid):
                end_left  = end_mid
            else:
                end_right = end_mid - 1

        if start_left >= self.len_nums and end_right <= 0:
            return [-1, -1]
        return [start_left, end_right]

    def start_boundary_condition(self, start_mid:int) -> bool:
        if start_mid == 0:
            return self.nums[start_mid] == self.target
        else:
            return self.nums[start_mid - 1] != self.target and self.nums[start_mid] == self.target
    
    def end_boundary_condition(self, end_mid:int) -> bool:
        if end_mid == self.len_nums - 1:
            return self.nums[end_mid] == self.target
        else:
            return self.nums[end_mid] == self.target and self.nums[end_mid + 1] != self.target