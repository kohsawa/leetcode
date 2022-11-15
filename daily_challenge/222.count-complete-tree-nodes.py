#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dig(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + dig(node.left) + dig(node.right)
        
        return dig(root)

        
# @lc code=end

