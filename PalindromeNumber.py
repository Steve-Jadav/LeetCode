class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
         
        i, reverse = 0, 0
        temp = x
        while (temp):
            reverse = (reverse * 10) + (temp % 10)
            temp = temp // 10
        
        return reverse == x
