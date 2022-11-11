#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                del nums[i + 1]
        return len(nums)

        
# @lc code=end

