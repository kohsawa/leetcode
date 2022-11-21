#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start
class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        route = [[-1 for _ in range(m)] for _ in range(n)]
        step = 0
        stack: set[tuple[int, int]] = set()
        stack.add(tuple(entrance))
        flag = False
        route[entrance[0]][entrance[1]] = 0

        while not flag and stack:
            step += 1
            for i, j in list(stack):
                stack.remove((i, j))

                if route[i][j] > 0 and (i == 0 or j == 0 or i == n - 1 or j == m - 1):
                    flag = True
                    break

                if i > 0 and maze[i - 1][j] == '.' and route[i - 1][j] < 0:
                    route[i - 1][j] = step
                    stack.add((i - 1, j))
                if i + 1 < n and maze[i + 1][j] == '.' and route[i + 1][j] < 0:
                    route[i + 1][j] = step
                    stack.add((i + 1, j))
                if j > 0 and maze[i][j - 1] == '.' and route[i][j - 1] < 0:
                    route[i][j - 1] = step
                    stack.add((i, j - 1))
                if j + 1 < m and maze[i][j + 1] == '.' and route[i][j + 1] < 0:
                    route[i][j + 1] = step
                    stack.add((i, j + 1))

        return step - 1 if flag else -1

# @lc code=end

