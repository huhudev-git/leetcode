#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []
        path = []
        self.find(root, 0, sum, path, result)
        return result

    def find(self, node, sum_, target, path, result):
        if node is None:
            return

        path.append(node.val)
        sum_ += node.val
        if node.left == None and node.right == None and sum_ == target:
            result.append(list(path))
            path.pop()
            return

        self.find(node.left, sum_, target, path, result)
        self.find(node.right, sum_, target, path, result)

        path.pop()
# @lc code=end
