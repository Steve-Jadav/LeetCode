class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singleNumber = 0
        for x in nums:
            singleNumber ^= x
        
        return singleNumber
