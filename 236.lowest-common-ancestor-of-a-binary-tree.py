#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = []
        self.find(root, p, q, result)
        return result[0]

    def find(self, node, p, q, result):
        if node is None or result:
            return None

        r = (node == p) or (node == q)
        r1 = self.find(node.left, p, q, result)
        if (r and r1):
            result.append(node)
            return

        r2 = self.find(node.right, p, q, result)
        if (r and r2):
            result.append(node)
            return

        if r1 and r2:
            result.append(node)
            return

        return r or r1 or r2
# @lc code=end

