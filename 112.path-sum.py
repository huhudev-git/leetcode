#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.find(root, 0, sum)

    def find(self, node, sum_, target):
        if node is None:
            return False

        sum_ += node.val
        if node.left == None and node.right == None and sum_ == target:
            return True

        if self.find(node.left, sum_, target):
            return True
        if self.find(node.right, sum_, target):
            return True
        return False


# @lc code=end
