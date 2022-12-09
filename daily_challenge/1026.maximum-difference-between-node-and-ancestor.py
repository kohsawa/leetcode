#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#

# @lc code=start
# Definition for a binary tree node.
class Solution:
    def maxAncestorDiff(self, root: TreeNode | None) -> int:
        def dig(root: TreeNode, maxVal: int = -1, minVal: int = 100001) -> int:
            maxVal = max(root.val, maxVal)
            minVal = min(root.val, minVal)
            res = abs(maxVal - minVal)

            if root.left:
                res = max(res, dig(root.left, maxVal, minVal))
            if root.right:
                res = max(res, dig(root.right, maxVal, minVal))
            return res

        return dig(root) if root else 0
        
# @lc code=end

