class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums == None:
            return None
        
        low, high = 0, len(nums) - 1
        
        if nums[low] <= nums[high]:
            return nums[low]
        
        while low <= high:
            
            mid = (low + high) // 2
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            if nums[mid] >= nums[high]:
                low = mid + 1
            
            else:
                high = mid - 1
