#
# @lc app=leetcode id=944 lang=python3
#
# [944] Delete Columns to Make Sorted
#

# @lc code=start
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        cnt = 0

        for i in range(m):
            for j in range(n - 1):
                if strs[j][i] > strs[j + 1][i]:
                    cnt += 1
                    break
        return cnt

# @lc code=end

