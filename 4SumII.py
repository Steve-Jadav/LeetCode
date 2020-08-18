class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
        hashmap = dict()
        totalTuples = 0
        
        for i in range(0, len(A)):
            for j in range(0, len(B)):
                sum = A[i] + B[j]
                
                if (sum in hashmap.keys()):
                    hashmap[sum] += 1
                else:
                    hashmap[sum] = 1
        
        for i in range(0, len(C)):
            for j in range(0, len(D)):
                sum = -(C[i] + D[j])
                
                if (sum in hashmap.keys()):
                    totalTuples += hashmap[sum]
        
        return totalTuples
