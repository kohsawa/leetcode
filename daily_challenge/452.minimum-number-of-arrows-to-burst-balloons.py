#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])
        cnt = 1
        tail = points[0][1]

        for s, e in points:
            if tail < s:
                tail = e
                cnt += 1
        return cnt

# @lc code=end

