#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        table = {}

        while head is not None:
            if table.get(head, False):
                return head
            table[head] = True
            head = head.next
        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        slow = head
        fast = head
        meet = None

        while fast:
            slow = slow.next

            fast = fast.next
            if fast is None:
                return None

            fast = fast.next
            if fast == slow:
                meet = fast
                break

        if meet is None:
            return None

        while True:
            if meet == head:
                return head
            meet = meet.next
            head = head.next
# @lc code=end
