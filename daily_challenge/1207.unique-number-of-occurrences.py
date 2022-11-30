#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#
from collections import Counter

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        return len(set(Counter(arr).values())) == len(set(arr))

# @lc code=end

