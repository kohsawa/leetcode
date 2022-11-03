#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            p = matrix[i][0]

            for j in range(n):
                if i + j < m and matrix[i + j][j] != p:
                    return False

        for j in range(n):
            p = matrix[0][j]

            for i in range(m):
                if j + i < n and matrix[i][j + i] != p:
                    return False

        return True


# @lc code=end

