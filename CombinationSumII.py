class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = list()
        self.backtrack(candidates, target, [], 0, 0, result)
        return result
    
    def backtrack(self, candidates, target, temp, tempSum, index, result):
        if tempSum > target:
            return 
        
        if tempSum == target:
            result.append(temp[:])
            return
        
        for i in range(index, len(candidates)):
            if (i > index and candidates[i] == candidates[i-1]) or candidates[i] > target:
                continue
            temp.append(candidates[i])
            self.backtrack(candidates, target, temp, tempSum + candidates[i], i + 1, result)
            temp.pop()
