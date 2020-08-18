# Problem 55

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        destinationIndex = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= destinationIndex:
                destinationIndex =  i
        
        return destinationIndex == 0
