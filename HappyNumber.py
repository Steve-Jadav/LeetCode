# Problem 202

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        hashset = set()
        hashset.add(n)
        newNumber = n
        
        while newNumber != 1:
            temp = 0
            
            while newNumber:
                temp += (newNumber % 10) ** 2
                newNumber = newNumber // 10
                
            newNumber = temp
            
            if newNumber in hashset:
                return False
            
            hashset.add(newNumber)
            
        return True
