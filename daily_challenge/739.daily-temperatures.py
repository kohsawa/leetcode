#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        st: list[int] = []
        res = [0] * len(temperatures)
        for i, j in enumerate(temperatures):
            while st and j > temperatures[st[-1]]:
                res[st[-1]] = i - st[-1]
                st.pop()            
            st.append(i)
        return res

# @lc code=end

