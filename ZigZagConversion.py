class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (s == None or len(s) == 0):
            return ""
    
        if (numRows == 1):
            return s
        
        result = [""] * numRows
        x, currentRow = 1, 0
        
        for i in range(0, len(s)):
            result[currentRow] += s[i]
            if numRows > 1:
                currentRow += x
                if currentRow == 0:
                    x = 1
                if currentRow == numRows - 1:
                    x = -1
        
        output = ""
        for j in range(0, numRows):
            output += result[j]
        
        return output
