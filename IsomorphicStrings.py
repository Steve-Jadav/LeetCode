class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = dict()
        hashset = set()
        
        for s_char, t_char in zip(s, t):
            if s_char not in hashmap.keys():
                if t_char not in hashset:
                    hashmap[s_char] = t_char
                    hashset.add(t_char)
                else:
                    return False
                
            else:
                if hashmap.get(s_char) != t_char:
                    return False
        
        return True
