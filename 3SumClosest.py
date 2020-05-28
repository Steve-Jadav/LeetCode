class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        n = len(nums)
        closest = float('inf')
        result = 0
        
        for i in range(0, n):
            
            left = i + 1
            right = n - 1
            
            while (left < right):
                total = nums[i] + nums[left] + nums[right]
                diff = abs(target - total)
                
                if (diff == 0):
                    return total
                
                if (diff < closest):
                    closest = diff
                    result = total
                    
                if (total <= target):
                    left += 1
                else:
                    right -=1
                
                
        return result
