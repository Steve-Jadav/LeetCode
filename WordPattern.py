# Problem 290

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if (len(pattern) == 0 or len(str) == 0):
            return False
        
        hashmap = dict()
        hashset = set()
        strings = str.split(" ")
        
        if (len(pattern) != len(strings)):
            return False
        
        for i in range(0, len(pattern)):
            if pattern[i] not in hashmap.keys():
                if strings[i] not in hashset:
                    hashmap[pattern[i]] = strings[i]
                    hashset.add(strings[i])
                else:
                    return False
            else:
                if hashmap.get(pattern[i]) != strings[i]:
                    return False
        
        return True
