# Problem 77

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = list()
        tempList = list()
        self.backtracking(n, k, 1, tempList, result)
        return result
    
    def backtracking(self, n, k, index, tempList, result):
        
        if len(tempList) == k:
            result.append(tempList[:])
            return
        
        for i in range(index, n + 1):
            tempList.append(i)
            self.backtracking(n, k, i + 1, tempList, result)
            tempList.pop()
