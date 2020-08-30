class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i in range(0, len(citations)):
            temp = len(citations) - i
            if temp <= citations[i]:
                return temp
       
        return 0
        
