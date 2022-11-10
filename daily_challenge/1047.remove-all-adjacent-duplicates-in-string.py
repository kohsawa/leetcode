#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        st: list[str] = []

        for c in s:
            if len(st) > 0 and st[-1] == c:
                st.pop()
            else:
                st.append(c)

        return "".join(st)
        
# @lc code=end

