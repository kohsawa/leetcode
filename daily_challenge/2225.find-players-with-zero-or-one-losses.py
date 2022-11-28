#
# @lc app=leetcode id=2225 lang=python3
#
# [2225] Find Players With Zero or One Losses
#
from itertools import chain

# @lc code=start
class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        N = max(chain(*matches))
        win = [100000] + [0] * N
        lose = [100000] + [0] * N
        
        for m in matches:
            win[m[0]] += 1
            lose[m[1]] += 1

        return [
            [i for i, v in enumerate(lose) if v == 0 and win[i] > 0],
            [i for i, v in enumerate(lose) if v == 1],
        ]

# @lc code=end
