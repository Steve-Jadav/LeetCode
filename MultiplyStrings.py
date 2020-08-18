# Problem 43

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        val1, val2 = 0, 0
        
        for i in range(0, len(num1)):
            curr = ord(num1[i]) - ord("0")
            val1 = (val1 * 10) + curr 
        
        for i in range(0, len(num2)):
            curr = ord(num2[i]) - ord("0")
            val2 = (val2 * 10) + curr
            
        integerResult = val1 * val2
        
        if integerResult == 0:
            return "0"
        
        stringResult = ""
        
        while integerResult:
            temp = integerResult % 10
            stringResult = chr(ord("0") + temp) + stringResult
            integerResult //= 10
            
        return stringResult
