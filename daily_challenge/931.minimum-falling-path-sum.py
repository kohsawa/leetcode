#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]

        dp = [[100000 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]

        for i in range(1, n):
            for j in range(n):
                dp[i][j] = min(
                    matrix[i][j] + dp[i -1][j - 1] if j > 0 else 100000,
                    matrix[i][j] + dp[i -1][j],
                    matrix[i][j] + dp[i -1][j + 1] if j < n - 1 else 100000,
                )

        return min(dp[n - 1])

# @lc code=end
