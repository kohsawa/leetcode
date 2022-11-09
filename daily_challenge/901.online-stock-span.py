#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
class StockSpanner:

    def __init__(self):
        self.stack: list[tuple[int, int]] = []
        self.day = 0
        

    def next(self, price: int) -> int:
        length = -1
        
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()

        if self.stack:
            length = self.stack[-1][0]

        res = self.day - length
        self.stack.append((self.day, price))
        self.day += 1
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

