#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.inorder(root, result)
        return result

    def inorder(self, node, result):
        if node == None:
            return

        self.inorder(node.left, result)
        result.append(node.val)
        self.inorder(node.right, result)

# @lc code=end
