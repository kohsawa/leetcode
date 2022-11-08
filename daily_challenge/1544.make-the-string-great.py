#
# @lc app=leetcode id=1544 lang=python3
#
# [1544] Make The String Great
#

# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        flag = True
        stack: list[str] = []

        for c in s:
            if len(stack) != 0 and (ord(stack[-1]) == ord(c) - 0x20 or ord(stack[-1]) == ord(c) + 0x20):
                stack.pop()
                flag = False

            if flag:
                stack.append(c)
            flag = True
        
        return "".join(stack)
# @lc code=end

