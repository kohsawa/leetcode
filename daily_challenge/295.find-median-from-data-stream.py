#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        self.nums: list[int]= []
        self.half_len: float = 0
        self.even = True
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.half_len += 0.5
        self.even = not self.even
        

    def findMedian(self) -> float:
        self.nums.sort()
        if self.even:
            return (self.nums[int(self.half_len - 0.5)] + self.nums[int(self.half_len + 0.5)]) / 2
        else:
            return self.nums[int(self.half_len)]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

