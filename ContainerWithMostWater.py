# Problem 11

class Solution:
    def maxArea(self, height: List[int]) -> int:
        minimum: int = 0
        maximum: int = 0
        i, j = 0, len(height) - 1
        
        while i != j:
            minimum = min(height[i], height[j])
            maximum = max(maximum, (j - i) * minimum)
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return maximum
