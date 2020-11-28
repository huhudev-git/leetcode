#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        origin_head = head

        while head:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            head = head.next
        return origin_head
# @lc code=end
