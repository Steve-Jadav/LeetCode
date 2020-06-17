class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """Problem 520"""
        allCaps = True
        noCaps = True
        firstCap = True
        
        for i in range(0, len(word)):
            if i == 0 and word[i].isupper():
                firstCap = True
            elif i != 0 and word[i].isupper():
                firstCap = False
                
            if word[i].islower():
                allCaps = False
            if word[i].isupper():
                noCaps = False
                
        return allCaps or noCaps or firstCap
