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


# Approach 2: Quick Select

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        unique = list()
        topK = list()
        
        for val in nums:
            if val in freq.keys():
                freq[val] += 1
            else:
                freq[val] = 1
    
        unique = list(freq.keys())
            
        self.quickSelect(0, len(unique) - 1, len(unique) - k, unique, freq)
    
        return unique[len(unique) - k:]
    
  
    def partition(self, low, high, unique, freq) -> int:
        
        pivot = unique[high]
        i = low - 1
        
        for j in range(low, high):
            if freq.get(unique[j]) <= freq.get(pivot):
                i += 1
                unique[i], unique[j] = unique[j], unique[i]
        
        unique[i+1], unique[high] = unique[high], unique[i+1]
        
        return i + 1
    
    
    def quickSelect(self, left, right, k_smallest, unique, freq):
        
        if left == right:
            return
        
        pivot_index = self.partition(left, right, unique, freq)
        
        if k_smallest == pivot_index:
            return
        
        elif k_smallest < pivot_index:
            self.quickSelect(left, pivot_index - 1, k_smallest, unique, freq)
            
        else:
            self.quickSelect(pivot_index + 1, right, k_smallest, unique, freq)


# Approach 3: Bucket Sort

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        freq = dict()
        topK = list()
        
        for val in nums:
            if val in freq.keys():
                freq[val] += 1
            else:
                freq[val] = 1
        
        for num, frequency in freq.items():
            bucket[frequency].append(num)
        
        for i in range(len(bucket) - 1, -1, -1):
            for j in range(len(bucket[i]) - 1, -1, -1):
                if (len(topK) < k):
                    topK.append(bucket[i][j])
                else:
                    break
        
        return topK
