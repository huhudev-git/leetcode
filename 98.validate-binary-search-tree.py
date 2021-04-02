#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self._isValidBST(root)

    def _isValidBST(self, root: TreeNode, left=None, right=None) -> bool:
        if not root:
            return True

        if left and left.val >= root.val:
            return False

        if right and right.val <= root.val:
            return False

        return self._isValidBST(root.left, left, root) and \
            self._isValidBST(root.right, root, right)
# @lc code=end
