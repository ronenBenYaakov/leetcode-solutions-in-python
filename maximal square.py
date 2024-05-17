class Solution(object):
    def maximalSquare(self, matrix):
        n, m, maximum = len(matrix), len(matrix[0]), 0
        dp =[[0] * m for i in range(n)]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                    maximum = 1

        for i in range(1, n):
            for j in range(1, m):
                if(dp[i][j - 1] > 0 and dp[i - 1][j] > 0 and dp[i - 1][j - 1] > 0 and dp[i][j] > 0):
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                maximum = max(maximum, dp[i][j] * dp[i][j])

        return maximum
        
