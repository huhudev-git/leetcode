#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        nodes = [root]
        self._connect(nodes)
        return root

    def _connect(self, nodes):
        next_level_nodes = []

        length = len(nodes)
        if length == 0:
            return

        for n in range(length - 1):
            nodes[n].next = nodes[n + 1]

        for n in nodes:
            if n.left:
                next_level_nodes.append(n.left)
            if n.right:
                next_level_nodes.append(n.right)

        self._connect(next_level_nodes)
# @lc code=end
