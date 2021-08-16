#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.loop(root, 0, [])

    def loop(self, root, total, item):
        if not root:
            return total

        if not (root.left or root.right):
            item.append(root.val)
            length = len(item) - 1
            for i, v in enumerate(item):
                total += v * (10 ** (length - i))
            item.pop()
            return total

        item.append(root.val)
        total = self.loop(root.left, total, item)
        total = self.loop(root.right, total, item)
        item.pop()
        return total


if __name__ == "__main__":
    s = Solution()
    print(s.sumNumbers(TreeNode(0, TreeNode(1))))
# @lc code=end
