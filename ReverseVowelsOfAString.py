class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'})
        start, end = 0, len(s) - 1
        string = list(s)
        while start < end:
            if string[start] not in vowels:
                start += 1
                continue
                
            if string[end] not in vowels:
                end -= 1
                continue
        
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1
        
        return ''.join(string)
