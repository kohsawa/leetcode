#
# @lc app=leetcode id=2136 lang=python3
#
# [2136] Earliest Possible Day of Full Bloom
#

# @lc code=start
class Solution:
    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:
        comb=[(plantTime[i],growTime[i]) for i in range(len(plantTime))]
        mx,passed_days=0,0
        comb.sort(key=lambda x:(-x[1],x[0]))
        for i in range(len(plantTime)):
            mx=max(mx,(passed_days+comb[i][0]+comb[i][1]))
            passed_days+=comb[i][0]
        return mx
        
# @lc code=end

