class Solution:
    
    def __binarySearch(self, i, matrix, target):
        if (len(matrix) == 0):
            return False
        
        low: int = 0
        high: int = len(matrix[i]) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if matrix[i][mid] == target:
                return True
            
            if matrix[i][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # []
        if (len(matrix) == 0):
            return False
        
        rows = len(matrix)
        columns = len(matrix[0])
        
        # [[]]
        if (columns == 0):
            return False
        
        for i in range(0, rows):
            if matrix[i][0] == target or matrix[i][columns - 1] == target:
                return True
            else:
                if self.__binarySearch(i, matrix, target):
                    return True
        
        return False
