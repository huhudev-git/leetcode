#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head is not None:
            # record next
            n = head.next

            # here think head is a element that is head of origin linked list
            # new_head is head of new linked list
            head.next = new_head
            new_head = head

            # become next
            head = n
        return new_head

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        x = head
        y = x.next
        x.next = None

        while y is not None:
            z = y.next
            y.next = x
            x = y
            y = z

        return x


# @lc code=end
