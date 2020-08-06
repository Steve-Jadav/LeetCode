# Problem 162
# Approach: O(n)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1
            

# Approach: Iterative Binary Search O(logn)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while (low < high):
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1
        
        return low
