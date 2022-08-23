#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root

        nodes = [root]
        self._connect(nodes)
        return root

    def _connect(self, nodes):
        if nodes[0] is None:
            return

        length = len(nodes)
        for n in range(length - 1):
            nodes[n].next = nodes[n + 1]

        next_level_nodes = []
        for n in nodes:
            next_level_nodes.append(n.left)
            next_level_nodes.append(n.right)

        self._connect(next_level_nodes)

# @lc code=end
