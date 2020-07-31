class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == None or len(matrix) == 0:
            return []
        
        top, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        direction = 0
        spiralOrder = list()
        
        while top <= down and left <= right:
            if direction == 0:
                for i in range(left, right + 1):
                    spiralOrder.append(matrix[top][i])
                top += 1
                direction = 1
            
            elif direction == 1:
                for i in range(top, down + 1):
                    spiralOrder.append(matrix[i][right])
                right -= 1
                direction = 2
                
            elif direction == 2:
                for i in range(right, left - 1, -1):
                    spiralOrder.append(matrix[down][i])
                down -= 1
                direction = 3
            
            else:
                for i in range(down, top - 1, -1):
                    spiralOrder.append(matrix[i][left])
                left += 1
                direction = 0
            
        return spiralOrder
