#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        pow2: list[int] = []
        i = 1
        while i ** 2 <= n:
            pow2.append(i ** 2)
            i += 1

        cnt = 0
        check: set[int] = {n}
        while len(check) > 0:
            cnt += 1
            tmp_check: set[int] = set()

            for item in check:
                for p in pow2:
                    if item == p:
                        return cnt
                    if item < p:
                        break
                    tmp_check.add(item - p)
            check = tmp_check

        return cnt

        
# @lc code=end

