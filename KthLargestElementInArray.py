# Quick Select

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums == None or len(nums) == 0:
            return -1
        
        n = len(nums)
        p = self.__partition(nums, 0, n - 1)
        
        low, high = 0, n - 1
        
        while n - p != k:
        
            if n - p > k:
                low = p + 1
                p = self.__partition(nums, p + 1, high)

            else:
                high = p - 1
                p = self.__partition(nums, low, p - 1)
        
        return nums[p]
        
    
    def __partition(self, nums: List[int], low: int, high: int) -> int:
        
        pivot = nums[high]
        i = low - 1
        
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                
        nums[i+1], nums[high] = nums[high], nums[i+1]
        
        return i + 1
