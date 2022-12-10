#
# @lc app=leetcode id=1339 lang=python3
#
# [1339] Maximum Product of Splitted Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class Solution:
    def maxProduct(self, root: TreeNode | None) -> int:
        sums: list[int] = []

        def sumSubTree(root: TreeNode | None) -> int:
            if not root:
                return 0
            sums.append(root.val + sumSubTree(root.left) + sumSubTree(root.right))
            return sums[-1]

        sumSubTree(root)
        sums.sort()
        root_sum = sums[-1]
        
        for i in range(len(sums)):
            if sums[i] >= root_sum // 2 and sums[i - 1] <= root_sum:
                return max(
                    sums[i - 1] * (root_sum - sums[i - 1]),
                    sums[i] * (root_sum - sums[i])
                ) % 1000000007

# @lc code=end

