class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        number1, number2 = 0, 0
        j = 0
        
        for i in range(len(num1) - 1, -1, -1):
            number1 += (ord(num1[i]) - ord('0')) * pow(10, j)
            j += 1
        
        j = 0
        for i in range(len(num2) - 1, -1, -1):
            number2 += (ord(num2[i]) - ord('0')) * pow(10, j)
            j += 1
        
        return str(number1 + number2)
