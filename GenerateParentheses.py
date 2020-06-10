class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        combinations = list()
        self.createBrackets("", combinations, n, n)
        return combinations
    
    def createBrackets(self, string, combinations, left, right):
        
        if left > right:
            return
        
        if left == 0 and right == 0:
            combinations.append(string)
            return
        
        if left > 0:
            self.createBrackets(string + "(", combinations, left - 1, right)
        if right > 0:
            self.createBrackets(string + ")", combinations, left, right - 1)
