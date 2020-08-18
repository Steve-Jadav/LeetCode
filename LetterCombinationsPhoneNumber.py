class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if (len(digits) == 0):
            return []
        
        result = list()
        
        self.mapper = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        self.__constructCombinations(digits, "", 0, result)
        return result
    
    def __constructCombinations(self, digits, curr, i, result):
        
        if i == len(digits):
            result.append(curr)
            return
        
        for index in self.mapper[digits[i]]:
            self.__constructCombinations(digits, curr + index, i + 1, result)
