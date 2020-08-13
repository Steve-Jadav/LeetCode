# Problem 560

# Approach: O(n2)
# Time Limit Exceeded

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count: int = 0
        
        for i in range(0, len(nums)):
            sum: int = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1
                    
        return count


# Approach: Hashmap

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = collections.defaultdict(int)
        hashmap.update( {0 : 1} )
        sum: int = 0
        count: int = 0
        for i in range(0, len(nums)):
            sum += nums[i]
            if (sum - k) in hashmap.keys():
                count += hashmap.get(sum - k)
            hashmap[sum] = hashmap[sum] + 1
        
        return count
