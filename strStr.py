class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if not haystack:
            return -1
        
        i = 0
        while i <= len(haystack) - len(needle):
            if haystack[i] == needle[0] and haystack[i + len(needle) - 1] == needle[-1]:
                if haystack[i:i+len(needle)] == needle:
                    return i
            i += 1
        
        return -1
