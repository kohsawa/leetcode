#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1, 2] + [0] * (n - 1)
        dp_bump = [1] * n
        
        for i in range(2, n):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp_bump[i - 1] * 2) % 1000000007
            dp_bump[i] = (dp[i - 2] + dp_bump[i - 1]) % 1000000007
        return dp[n - 1]

# @lc code=end

