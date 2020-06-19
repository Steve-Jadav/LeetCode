# Problem 62

class Solution:
    """ This version calculates the total number of unique
    as wells as the paths themselves. Recursion."""

    def uniquePaths(self, m: int, n: int) -> int:
        self.paths = 0
        self.result = list()
        self.getPaths(0, 0, m, n, [(0,0)])
        print (self.result)
        return self.paths

    def getPaths(self, x: int, y: int, m: int, n: int, path: List):
        if y == m - 1 and x == n - 1:
            self.paths += 1
            self.result.append(path)
            return

        if y < m - 1:
            self.getPaths(x, y + 1, m, n, path + [(x, y+1)])
        if x < n - 1:
            self.getPaths(x + 1, y, m, n, path + [(x+1, y)])

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# APPROACH 2: Dynamic Programming

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m columns, n rows
        dp = [[0 for x in range(0, m)] for x in range(0, n)]

        for i in range(0, m):
            dp[0][i] = 1

        for i in range(0, n):
            dp[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[n-1][m-1]
