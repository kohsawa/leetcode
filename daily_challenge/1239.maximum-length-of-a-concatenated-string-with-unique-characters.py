#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#

# @lc code=start
class Solution:
    def maxLength(self, arr: list[str]) -> int:
        S = [""]
        l = 0
        for w in arr:
            for s in S:
                new_s = s + w
                
                if len(new_s) != len(set(new_s)):
                    continue
                
                S.append(new_s)
                l = max(l, len(new_s))

        return l
# @lc code=end

