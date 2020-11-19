#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        origin_head = head

        new_head = None
        pre_head = None

        # move to m
        for _ in range(m-1):
            pre_head = head
            head = head.next

        # the node which is the last node in reversed linked list
        reversed_last = head

        new_head = None
        move = n - m + 1
        while head is not None and move:
            n = head.next
            head.next = new_head
            new_head = head
            head = n

            move -= 1

        # now head is the n index node
        reversed_last.next = head

        # connect to pre head
        if pre_head is not None:
            pre_head.next = new_head
        else:
            return new_head
        return origin_head

# @lc code=end
