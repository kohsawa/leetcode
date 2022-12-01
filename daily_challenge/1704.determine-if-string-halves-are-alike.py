#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#

# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        return len(list(filter(lambda c: c in ["a", "e", "i", "o", "u"], s[:len(s)//2]))) == len(list(filter(lambda c: c in ["a", "e", "i", "o", "u"], s[len(s)//2:])))

# @lc code=end
