# Problem 1513

class Solution:
    def numSub(self, s: str) -> int:
        if s == None or len(s) == 0:
            return 0
        
        count = 0
        temp = s.split("0")
        
        for t in temp:
            if len(t) > 0:
                k = len(t)
                count += ((k * (k + 1)) // 2)
        
        return count % (pow(10, 9) + 7)
