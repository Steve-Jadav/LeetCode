class Solution:
    def __init__(self):
        pass
    
    def missingNumber(self, nums: list[int]) -> int:
        """
        Given an array nums containing n distinct numbers in the range [0, n], 
        returns the only number in the range that is missing from the array.

        Args:
            nums (list[int]): List of integers.

        Returns:
            int: The number in the range [0, n] that is missing from the given array.
        """
        
        if nums is None or len(nums) == 0:
            return 0

        n = len(nums)
        expected_sum = (n*(n+1))/2
        existing_sum = sum(nums)
        return int(expected_sum - existing_sum)
    

if __name__ == "__main__":
    solution = Solution()
    res = solution.missingNumber(
        [1,2]
    )
    
    print (res)