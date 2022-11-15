#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#
from collections import defaultdict

# @lc code=start
class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        def remove_point(X: int, Y: int):
            points.discard((X, Y))

            for y in x_dict[X]:
                if (X, y) in points:
                    remove_point(X, y)

            for x in y_dict[Y]:
                if (x, Y) in points:
                    remove_point(x, Y)


        x_dict: dict[int, list[int]] = defaultdict(list)
        y_dict: dict[int, list[int]] = defaultdict(list)
        points: set[tuple[int, int]] = {(s[0], s[1]) for s in stones}
        count = 0
        
        for s in stones:
            x_dict[s[0]].append(s[1])
            y_dict[s[1]].append(s[0])

        for s in stones:
            X = s[0]
            Y = s[1]

            if (X, Y) in points:
                remove_point(X, Y)
                count += 1

        return len(stones) - count

        
# @lc code=end

