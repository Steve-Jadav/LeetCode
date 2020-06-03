class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry: int = 0
        n: int = len(digits)
        
        for i in range(n-1, -1, -1):
            val = digits[i] + 1
            if val > 9:
                digits[i] = 0
                
                if i == 0:
                    digits.insert(0, 1)
            
            else:
                digits[i] += 1
                break
        
        return digits
