#
# @lc app=leetcode id=1833 lang=python3
#
# [1833] Maximum Ice Cream Bars
#

# @lc code=start
class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        c = 0
        for i in sorted(costs):
            if coins >= i:
                c += 1
                coins -= i
        return c

# @lc code=end

