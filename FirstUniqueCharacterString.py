# Problem 387

class Solution:
    def firstUniqChar(self, s: str) -> int:
        idx = -1
        hashmap = dict()
        
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        
        for i in range(0, len(s)):
            if hashmap[s[i]] == 1:
                idx = i
                break
        
        return idx
