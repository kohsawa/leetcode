#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        for i in range(3, -1, -1):
            if (num // (10 ** i) % 10) == 6:
                num += 3 * (10 ** i)
                break
        return num

# @lc code=end
