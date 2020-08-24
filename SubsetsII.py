# Problem 90

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 or nums == None:
            return []
        
        nums.sort()
        result = list()
        temp = list()
        self.backtracking(nums, 0, temp, result)
        return result
    
    def backtracking(self, nums: List[int], index: int, temp: List[int], result: List[List[int]]):
        
        result.append(temp[:])

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            temp.append(nums[i])
            self.backtracking(nums, i + 1, temp, result)
            temp.pop()
