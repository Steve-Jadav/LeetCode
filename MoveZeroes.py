class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Approach 1: Requires more swap operations. Find the location
        of the first zero element and perform swap operations thereafter.
        Complexity: O(n)
        """
        if (nums == None or len(nums) == 0):
            return 0

        i = 0
        while i < len(nums):
            if nums[i] == 0:
                break
            i += 1

        for j in range(i + 1, len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

    def moveZeroes2(self, nums: List[int]) -> None:
            """
            Do not return anything, modify nums in-place instead.
            Approach 2: No swap required. Copy all the non-zero
            elements to the front of the array, and set the remaining
            elements to 0.
            Complexity: O(n)
            """
            if (nums == None or len(nums) == 0):
                return 0

            i = 0
            for j in range(0, len(nums)):
                if nums[j] != 0:
                    nums[i] = nums[j]
                    i += 1

            for j in range(i, len(nums)):
                nums[j] = 0
