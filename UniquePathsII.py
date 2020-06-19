# Problem 63.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m: int = len(obstacleGrid)
        n: int = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            obstacleGrid[0][0] = 0
        else:
            obstacleGrid[0][0] = 1
        
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]
            
        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = 0
            else:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        
        return obstacleGrid[m-1][n-1]
