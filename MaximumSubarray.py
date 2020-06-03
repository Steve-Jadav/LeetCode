class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        p = 0
        current_max = float('-inf')
        
        for i in range(0, len(nums)):
            p = max(p + nums[i], nums[i])
            current_max = max(current_max, p)
        
        return current_max
