# Problem 1010

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs = 0
        hashmap = collections.defaultdict(int)
        for val in time:
            d = (60 - (val % 60)) % 60
            pairs += hashmap[d]
            hashmap[val % 60] += 1
        
        return pairs
