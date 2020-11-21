#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result

        if root.left is None and root.right is None:
            result.append(root.val)
            return result

        root.level = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node.level == len(result):
                result.append(node.val)
            else:
                result[node.level] = node.val

            if node.right:
                node.right.level = node.level + 1
                stack.append(node.right)
            if node.left:
                node.left.level = node.level + 1
                stack.append(node.left)

        return result


# @lc code=end
