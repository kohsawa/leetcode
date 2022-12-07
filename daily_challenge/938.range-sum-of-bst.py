#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        sum = root.val if low <= root.val <= high else 0
        sum += (
            self.rangeSumBST(root.right, low, high)
            if root.val <= low
            else self.rangeSumBST(root.left, low, high)
            if root.val >= high
            else (
                self.rangeSumBST(root.right, low, high)
                + self.rangeSumBST(root.left, low, high)
            )
        )

        return sum


# @lc code=end
