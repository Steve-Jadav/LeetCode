# Problem 347

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        hashmap = dict()
        
        for x in nums:
            if x in hashmap.keys():
                hashmap[x] += 1
            else:
                hashmap[x] = 1
                
        return heapq.nlargest(k, hashmap.keys(), key=hashmap.get)
