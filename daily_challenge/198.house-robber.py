#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        dp = nums[:2] + [-1] * (n - 2)
        for i in range(2, n):
            dp[i] = max(dp[:i - 1]) + nums[i]

        return max(dp)

# @lc code=end

