# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
	Problem 278.
        """
        low: int = 1
        high: int = n
        mid: int = (low + high)//2
        
        while low <= high:
            mid = (low + high)//2
            if (isBadVersion(mid)):
                high = mid - 1
            else:
                low = mid + 1
        
        if(isBadVersion(mid)):
            return mid
        else:
            return mid + 1
        
