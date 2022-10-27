#
# @lc app=leetcode id=835 lang=python3
#
# [835] Image Overlap
#

# @lc code=start
class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        N = len(img1)
        img1_1: list[tuple[int, int]] = []
        img2_1: list[tuple[int, int]] = []

        for i in range(N):
            for j in range(N):
                if img1[i][j] == 1:
                    img1_1.append((i, j))
        
                if img2[i][j] == 1:
                    img2_1.append((i, j))
        
        dist_sum: dict[tuple[int, int], int] = dict()

        for x1, y1 in img1_1:
            for x2, y2 in img2_1:
                d = (x2 - x1, y2 - y1)

                if d in dist_sum.keys():
                    dist_sum[d] += 1
                else:
                    dist_sum[d] = 1
        return max(dist_sum.values()) if len(dist_sum) else 0
# @lc code=end

