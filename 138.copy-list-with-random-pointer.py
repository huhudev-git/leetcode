#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if head is None:
            return None

        table = {}

        # create a table
        # record origin node index
        t = head
        index = 0
        while t is not None:
            table[t] = index
            index += 1
            t = t.next

        # create a new linked list
        t = head
        new_list = []
        while t is not None:
            n = Node(t.val, None, None)
            t = t.next
            new_list.append(n)

        # last is None
        new_list.append(None)
        table[None] = len(new_list) - 1

        t = head
        n = new_list[0]
        while t is not None:
            # index
            index = table[t.next]
            n.next = new_list[index]

            if t.random is not None:
                index = table[t.random]
                n.random = new_list[index]
            else:
                n.random = None

            n = n.next
            t = t.next

        return new_list[0]

# @lc code=end
