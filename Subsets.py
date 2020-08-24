# Problem 78

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if nums == None or len(nums) == 0:
            return []
        
        result = list()
        temp = list()
        self.backtracking(nums, 0, temp, result)
        return result
        
    def backtracking(self, nums: List[int], index: int, temp: List[int], result: List[int]):
        result.append(temp[:])
        for i in range(index, len(nums)):
            temp.append(nums[i])
            self.backtracking(nums, i + 1, temp, result)
            temp.pop()
        
