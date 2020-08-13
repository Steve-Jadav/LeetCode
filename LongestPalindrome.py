class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0

        for v in collections.Counter(s).values():
            result += v // 2 * 2
            
            if (result % 2 == 0 and v % 2 == 1):
                result += 1
        
        return result
