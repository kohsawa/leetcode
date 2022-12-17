#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st: list[int] = []

        for token in tokens:
            if token in "+-*/":
                a, b = st[-2:]
                res = a + b if token == "+" else a - b if token == "-" else a * b if token == "*" else (int)(a / b)
                st = st[:-2] + [res]
            else:
                st.append(int(token))
        return st[0]

# @lc code=end

