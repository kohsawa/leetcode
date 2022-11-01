#
# @lc app=leetcode id=1706 lang=python3
#
# [1706] Where Will the Ball Fall
#

# @lc code=start
class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m = len(grid)
        n = len(grid[0])
        answer = [0] * n

        for j in range(n):
            k = j

            for i in range(m):
                s = grid[i][k]

                if (k == 0 and s == -1) or (k == n - 1 and s == 1) or s != grid[i][k + s]:
                    k = -1
                    break
                
                k += s
            answer[j] = k
        
        return answer
# @lc code=end

