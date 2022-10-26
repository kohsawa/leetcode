#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        sums = {0: -1}
        cumulative_sum = 0

        for i, num in enumerate(nums):
            cumulative_sum += num
            rem = cumulative_sum % k

            if rem in sums and i - sums[rem] >= 2:
                return True

            if rem not in sums:
                sums[rem] = i

        return False

        
# @lc code=end

