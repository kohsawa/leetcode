#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#

# @lc code=start
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        res = (ay2 - ay1) * (ax2 - ax1) + (by2 - by1) * (bx2 - bx1)
        return res - (min(ax2, bx2) - max(ax1, bx1)) * (min(ay2, by2) - max(ay1, by1)) if ax1 < bx2 and  bx1 < ax2 and ay1 < by2 and by1 < ay2 else res
        
# @lc code=end

