class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """ Time complexity: O(nlogn) """
        if (nums == None or len(nums) == 0):
            return 1
    
        nums = list(set(nums))
        nums.sort()
        
        missing = 1
        
        for i in range(0, len(nums)):
            if nums[i] <= 0:
                continue
                
            if nums[i] == missing:
                missing += 1
            else:
                return missing
        
        return missing
