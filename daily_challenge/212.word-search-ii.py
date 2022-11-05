#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        c_map: dict[str, list[tuple[int, int]]] = dict()
        exists: list[str] = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (c := board[i][j]) in c_map:
                    c_map[c].append((i, j))
                else:
                    c_map[c] = [(i, j)]

        for w in words:
            for c in w:
                if c not in c_map:
                    break

                for p in c_map[c]:
                    

        return exists

# @lc code=end

