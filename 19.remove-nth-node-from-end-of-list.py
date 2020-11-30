#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        origin_head = head

        index = self.gen(head, n + 1)

        if index == n:
            return head.next
        return origin_head

    def gen(self, node, n):
        if not node:
            return 0

        index = self.gen(node.next, n) + 1
        # print(index, node.val, n)
        if index == n:
            node.next = node.next.next
        return index

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head

        # new -> head
        p2 = ListNode(-1)
        p2.next = head
        # newhead -> head
        head = p2

        # p2 and p1 between n
        # p2 -----n-----> p1
        for _ in range(0, n):
            p1 = p1.next

        while p1 != None:
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next
        return head.next

    def removeNthFromFront(self, head: ListNode, n: int) -> ListNode:
        origin_head = head
        for _ in range(n - 1):
            head = head.next

        if head and head.next:
            head.next = head.next.next
        return origin_head

# @lc code=end
