class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """ Time complexity: O(nlogn) """
        if (nums == None or len(nums) == 0):
            return 1

        nums.sort()

        missing = 1

        for i in range(0, len(nums)):
            if nums[i] <= 0:
                continue
	
	    if i > 0 and nums[i] == nums[i - 1]:
		continue

            if nums[i] == missing:
                missing += 1
            else:
                return missing

        return missing


    def firstMissingPositive(self, nums: List[int]) -> int:
        """ Time complexity: O(n) """
        n = len(nums)
        nums = set(nums)
        missing = n + 1

        for i in range(1, n+1):
            if i not in nums:
                return i

        return missing
