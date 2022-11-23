#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            line1 = list(filter(lambda p: p != ".", board[i]))
            line2 = [l[i] for l in board if l[i] != "."]
            if len(line1) != len(set(line1)) or len(line2) != len(set(line2)):
                return False

        for i in range(3):
            for j in range(3):
                line: list[str] = []
                for l in board[i * 3 : (i + 1) * 3]:
                    line.extend(list(filter(lambda p: p != ".", l[j * 3 : (j + 1) * 3])))
                if len(line) != len(set(line)):
                    return False
        return True

# @lc code=end

