#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        s_list = list(s)
        
        for c in s_list:
            if c in "aeiouAEIOU":
                vowels.append(c)
        
        for i in range(len(s_list)):
            if s_list[i] in "aeiouAEIOU":
                s_list[i] = vowels.pop(-1)
        return "".join(s_list)
        
# @lc code=end

