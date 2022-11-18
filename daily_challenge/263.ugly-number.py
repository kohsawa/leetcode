#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        for d in [2, 3, 5]:
            while n > 1 and n % d == 0:
                n //= d
        
        return n == 1
        
# @lc code=end

