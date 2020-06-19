# Problem 64

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        "Recursion: Time limit exceeded."

        self.minSum = float('inf')
        self.findMinPathSum(grid, 0, 0, grid[0][0])
        return self.minSum

    def findMinPathSum(self, grid, i, j, currentSum):
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            self.minSum = min(self.minSum, currentSum)
            return

        if j < len(grid[0]) - 1:
            self.findMinPathSum(grid, i, j + 1, currentSum + grid[i][j+1])

        if i < len(grid) - 1:
            self.findMinPathSum(grid, i + 1, j, currentSum + grid[i+1][j])


# Problem 64
# DP
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """ Approach: Dynamic Programming """
        if (grid == None or len(grid) == 0):
            return 0

        dp = [[0 for x in range(len(grid[0]))] for x in range(len(grid))]

        for i in range(0, len(dp)):
            for j in range(0, len(dp[i])):
                dp[i][j] += grid[i][j]

                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1])
                elif i > 0:
                    dp[i][j] += dp[i-1][j]
                elif j > 0:
                    dp[i][j] += dp[i][j-1]

        return dp[len(dp) - 1][len(dp[0]) - 1]
