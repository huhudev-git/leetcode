#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return None

        less = lesshead = None
        last = pos = head

        while pos is not None:
            if pos.val < x:
                if lesshead is None:
                    lesshead = pos
                else:
                    less.next = pos

                less = pos

                if head == pos:
                    last = head = pos.next
                else:
                    last.next = pos.next
            else:
                last = pos

            pos = pos.next

        if lesshead is not None:
            less.next = head
        else:
            lesshead = head
        return lesshead

    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return None

        less = []
        large = []

        while head is not None:
            if head.val >= x:
                large.append(head)
            else:
                less.append(head)
            head = head.next

        if large:
            for i in range(1, len(large)):
                large[i - 1].next = large[i]
            large[-1].next = None

        if less:
            for i in range(1, len(less)):
                less[i - 1].next = less[i]

            if large:
                less[-1].next = large[0]
            else:
                less[-1].next = None
            return less[0]
        return large[0]
# @lc code=end
