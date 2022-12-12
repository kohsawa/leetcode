#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        c, b = 1, 1
        i = 1
        while i < n:
            tmp = c
            c += b
            b = tmp
            i += 1
        return c

# @lc code=end

