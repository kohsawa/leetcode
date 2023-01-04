#
# @lc app=leetcode id=2244 lang=python3
#
# [2244] Minimum Rounds to Complete All Tasks
#
from collections import Counter

# @lc code=start
class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        c = Counter(tasks)
        r = 0

        for i  in c.values():
            if i == 1:
                r = -1
                break
            r += i // 3 + (i % 3 > 0)
        return r

# @lc code=end

