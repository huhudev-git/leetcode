#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_head = ListNode()
        new_head.next = head

        last = new_head
        while head:
            isDup = False
            while head.next and head.val == head.next.val:
                isDup = True
                head.next = head.next.next

            if isDup:
                last.next = head.next
            else:
                last = head
            head = head.next
        return new_head.next
# @lc code=end
