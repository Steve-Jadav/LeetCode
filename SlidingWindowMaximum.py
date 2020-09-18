# Problem 239
# Approach: deque

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if (nums == None or len(nums) == 0 or k > len(nums)):
            return []
        
        result = list()
        deck = deque([])
        
        for i in range(0, len(nums)):

            if deck and deck[0] == i - k:
                deck.popleft()
            
            while (deck and nums[deck[-1]] <= nums[i]):
                deck.pop()
            
            deck.append(i)
            
            if (i >= k - 1):
                result.append(nums[deck[0]])
        
        return result
