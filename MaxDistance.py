def maxDistance(nums):
    if nums is None or len(nums) == 0:
        return 0

    hashmap = dict()
    maxDist = 0

    for i in range(0, len(nums)):
        if nums[i] not in hashmap:
            hashmap[nums[i]] = i
        else:
            hashmap[nums[i]] = i - hashmap[nums[i]]
            maxDist = max(maxDist, hashmap[nums[i]])
    
    return maxDist

print (maxDistance([1,2,3,4,3,1,10,11,12,13,14,15,16,2]))
print (maxDistance([1,2,1,2]))