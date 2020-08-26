# Problem 189

# Approach 1
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        for _ in range(0, k):
            self.rightRotate(nums)
                
        return nums
    
    def rightRotate(self, nums: List[int]):
        temp = nums[-1]
        for i in range(len(nums) - 1, 0, -1):
            nums[i] = nums[i-1]
        nums[0] = temp


# Approach 2
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
