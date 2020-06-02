class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        stack = list()
        
        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif stack and s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif stack and s[i] == '}' and stack[-1] == '{':
                stack.pop()
            elif stack and s[i] == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
        
        if stack:
            return False
        
        return True
