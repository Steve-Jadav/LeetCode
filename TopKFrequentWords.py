import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        topK = list()
        freq = dict()
        maxHeap = list()
        heapq.heapify(maxHeap)
        
        for w in words:
            if w in freq.keys():
                freq[w] += 1
            else:
                freq[w] = 1
        
        for w in freq.keys():
            heapq.heappush(maxHeap, (-freq[w], w))
            
        for i in range(0, k):
            topK.append(heapq.heappop(maxHeap)[1])
        
        return topK
        
