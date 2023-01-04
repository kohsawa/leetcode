#
# @lc app=leetcode id=2244 lang=python3
#
# [2244] Minimum Rounds to Complete All Tasks
#

# @lc code=start
class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        c = Counter(tasks)
        r = 0

        for i  in c.values():
            if i == 1:
                return -1
            r += (i + 2) // 3
        return r

# @lc code=end

