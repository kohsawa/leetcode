#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d: dict[str, list[str]] = dict()

        for s in strs:
            s_r = "".join(sorted(s))
            if s_r in d.keys():
                d[s_r].append(s)
            else:
                d[s_r] = [s]
        return d.values()

# @lc code=end
