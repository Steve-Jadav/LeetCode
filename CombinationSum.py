class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        self.backtracking(candidates, 0, 0, target, [], result)
        return result
    
    def backtracking(self, candidates, index, tempSum, target, temp, result):
        
        if tempSum > target:
            return
        
        if tempSum == target:
            result.append(temp[:])
            return
        
        for i in range(index, len(candidates)):
            temp.append(candidates[i])
            self.backtracking(candidates, i, tempSum + candidates[i], target, temp, result)
            temp.pop()
