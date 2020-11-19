#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        table = {}

        while head is not None:
            if table.get(head, False):
                return True
            table[head] = True
            head = head.next
        return False

    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        slow = head
        fast = head

        while fast:
            slow = slow.next

            fast = fast.next
            if fast is None:
                return False

            fast = fast.next
            if fast == slow:
                return True

        return False

# @lc code=end
