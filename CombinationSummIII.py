# Problem 216

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        hashset = set()
        result = list()
        self.backtrack(k, n, 1, 0, hashset, [], result)
        return result
    
    def backtrack(self, k: int, n: int, index: int, total: int, hashset, temp, result):
        
        if len(temp) > k:
            return
        
        if len(temp) == k and total == n:
            result.append(temp[:])
            return
        
        for i in range(index, 10):
            if i in hashset:
                continue
            temp.append(i)
            hashset.add(i)
            total += i
            self.backtrack(k, n, i + 1, total, hashset, temp, result)
            total -= i
            hashset.remove(i)
            temp.pop()
