class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        string = list(s)
        index = 0
        
        while index < len(string):
            start = index
            end = min(index + k - 1, len(string) - 1)
            
            while start < end:
                string[start], string[end] = string[end], string[start]
                start += 1
                end -= 1
                
            index += 2*k
            
        return ''.join(string)
        
