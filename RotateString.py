class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        max_rotations = len(s)
        curr = s

        while max_rotations != 0:
            curr = self.rotateLeft(curr)
            if curr == goal:
                return True

        return False
    
    def rotateLeft(self, s: str) -> str:
        if s is None or len(s) == 0:
            return ""
        
        firstChar = s[0]
        rotated_string = list()
        for i in range(1, len(s)):
            rotated_string.append(s[i])
        
        rotated_string.append(firstChar)
        return ''.join(rotated_string)
    
    
if __name__ == "__main__":
    solution = Solution()
    res = solution.rotateString("steve", "evst")
    print (res)