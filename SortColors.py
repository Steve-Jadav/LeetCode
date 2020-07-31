class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if (len(nums) == 0 or len(nums) == 1):
            return 
        
        start = 0
        end = len(nums) - 1
        current = 0
        
        while (current <= end and start < end):
            if nums[current] == 0:
                nums[current] = nums[start]
                nums[start] = 0
                start += 1
                current += 1
                
            elif nums[current] == 2:
                nums[current] = nums[end]
                nums[end] = 2
                end -= 1
            
            else:
                current += 1
