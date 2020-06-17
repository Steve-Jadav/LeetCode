class Solution:
    def toLowerCase(self, str: str) -> str:
        """Problem 709"""
        if str == None or len(str) == 0:
            return ""
        
        lower = list()
        for s in str:

            if ord(s) < 91 and ord(s) >= 65:
                lower.append(chr(ord(s) + 32))
            else:
                lower.append(s)
        return ''.join(lower)
