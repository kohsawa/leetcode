#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(list(filter(lambda x: x is not '', s.split(" ")))))
        
# @lc code=end

