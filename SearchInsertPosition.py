class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """ Runtime: O(n) """

        if (nums == None or len(nums) == 0):
            return 0

        insert_pos: int = 0

        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                insert_pos = i + 1
            else:
                break

        return insert_pos


    def searchInsert(self, nums: List[int], target: int) -> int:
            """ Runtime: O(log(n)) using Binary Search"""

            if (nums == None or len(nums) == 0):
                return 0

            low: int = 0
            high: int = len(nums) - 1
            insert_pos: int = 0

            while low <= high:
                mid: int = (low + high)//2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    high = mid - 1
                    insert_pos = mid
                else:
                    low = mid + 1
                    insert_pos = mid + 1

            return insert_pos
