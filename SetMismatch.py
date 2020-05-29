class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing = sum([i for i in range(1, len(nums)+1)]) - sum(set(nums))
        counts = sum(nums)-sum(set(nums))
        return [counts, missing]
