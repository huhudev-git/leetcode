#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True

        if not (root.left and root.right):
            return False

        arr1 = []
        arr2 = []
        self.left(root.left, arr1)
        self.right(root.right, arr2)

        if len(arr1) != len(arr2):
            return False

        for i, j in zip(arr1, arr2):
            if i != j:
                return False
        return True

    def left(self, node, arr):
        if node is None:
            arr.append(-101)
            return

        arr.append(node.val)
        self.left(node.left, arr)
        self.left(node.right, arr)

    def right(self, node, arr):
        if node is None:
            arr.append(-101)
            return

        arr.append(node.val)
        self.right(node.right, arr)
        self.right(node.left, arr)

# @lc code=end
