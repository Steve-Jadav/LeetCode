# Problem 347
# In order to implement a max heap in python, simply multiply each val by -1.
# This will transform a minheap into a maxheap.

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        freq = dict()
        maxHeap = list()
        topK = list()
        
        for val in nums:
            if val in freq.keys():
                freq[val] += 1
            else:
                freq[val] = 1
        
        heapq.heapify(maxHeap)
        
        for key in freq.keys():
            heapq.heappush(maxHeap,(-freq[key], key))
        
        for i in range(0, k):
            topK.append(heapq.heappop(maxHeap)[1])
        
        return topK
