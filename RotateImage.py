class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose
        for i in range(0, len(matrix)):
            for j in range(i, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
	# Reverse each row
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix[i]) - j - 1]
                matrix[i][len(matrix[i]) - j - 1] = temp
                
        
        
