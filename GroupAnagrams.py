from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for string in strs:
            dictionary[''.join(sorted(string))].append(string)
        return list(dictionary.values())
