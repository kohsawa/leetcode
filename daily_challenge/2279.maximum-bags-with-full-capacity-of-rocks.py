#
# @lc app=leetcode id=2279 lang=python3
#
# [2279] Maximum Bags With Full Capacity of Rocks
#

# @lc code=start
class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        n = len(capacity)
        rem: list[int] = [0] * n
        
        for i in range(n):
            rem[i] = capacity[i] - rocks[i]

        cnt = 0
        for r in sorted(rem):
            if r > additionalRocks:
                break
            additionalRocks -= r
            cnt += 1
        return cnt

# @lc code=end

