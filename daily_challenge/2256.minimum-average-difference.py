#
# @lc app=leetcode id=2256 lang=python3
#
# [2256] Minimum Average Difference
#

# @lc code=start
class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        N = len(nums)
        sums: list[int] = [0] * (N + 1)

        for i in range(1, N + 1):
            sums[i] = nums[i - 1] + sums[i - 1]

        avgs: list[int] = [100000] * (N)
        for i in range(1, N + 1):
            avgs[i - 1] = abs((sums[i] - sums[0]) // i - ((sums[N] - sums[i]) // (N - i) if i != N else 0))

        ans = 100000
        idx = 0
        for i in range(N):
            if ans > avgs[i]:
                ans = avgs[i]
                idx = i
        return idx

# @lc code=end

