# Problem 46

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == None or len(nums) == 0:
            return []
        
        result = list()
        temp = list()
        hashset = set()
        self.backtracking(nums, 0, hashset, temp, result)
        return result
    
    def backtracking(self, nums: List[int], index: int, hashset: set(), temp: List[int], result: List[List[int]]):
        
        if len(temp) == len(nums):
            result.append(temp[:])
            return
            
        for i in range(0, len(nums)):
            if nums[i] in hashset:
                continue
            else:
                temp.append(nums[i])
                hashset.add(nums[i])
                self.backtracking(nums, i + 1, hashset, temp, result)
                hashset.remove(nums[i])
                temp.pop()
