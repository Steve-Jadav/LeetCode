# Problem 131

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()
        hashset = set()
        self.backtrack(nums, [], hashset, result)
        return result
    
    def backtrack(self, nums, temp, hashset, result):
        
        if len(temp) == len(nums):
            result.append(temp[:])
            return
        
        else:
            for i in range(0, len(nums)):
                if nums[i] in hashset:
                    continue
                temp.append(nums[i])
                hashset.add(nums[i])
                self.backtrack(nums, temp, hashset, result)
                temp.pop()
                hashset.remove(nums[i])
