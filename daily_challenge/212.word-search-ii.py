#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
from functools import reduce
from collections import defaultdict
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # create trie
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = True

        for word in words:
            reduce(dict.__getitem__,word,trie)[END] = word

        res = set()
        def findstr(i,j,t):
            if END in t:
                res.add(t[END])
                # return
            letter = board[i][j]
            board[i][j] = ""
            if i > 0 and board[i-1][j] in t:
                findstr(i-1,j,t[board[i-1][j]])
            if j>0 and board[i][j-1] in t:
                findstr(i,j-1,t[board[i][j-1]])
            if i < len(board)-1 and board[i+1][j] in t:
                findstr(i+1,j,t[board[i+1][j]])
            if j < len(board[0])-1 and board[i][j+1] in t:
                findstr(i,j+1,t[board[i][j+1]])
            board[i][j] = letter

            return 

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if board[i][j] in trie:
                    findstr(i,j,trie[board[i][j]])
        return res

# @lc code=end

