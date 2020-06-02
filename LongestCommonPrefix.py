class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        
        strs.sort()
        prefix = ""
        length = min(len(strs[0]), len(strs[-1]))
        
        for i in range(0, length):
            if strs[0][i] == strs[-1][i]:
                prefix += strs[0][i]
            else:
                break
        
        return prefix
