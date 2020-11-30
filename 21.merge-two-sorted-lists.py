#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        new = ListNode()
        origin_l1 = l1
        origin_l2 = l2
        pre_l1 = l1
        pre_l2 = l2

        while l1 and l2:
            if l2.val > l1.val:
                new.next = l1
                new = new.next
                pre_l1 = l1
                l1 = l1.next
            else:
                new.next = l2
                new = new.next
                pre_l2 = l2
                l2 = l2.next

        if l2 is not None:
            pre_l1.next = l2
        elif l1 is not None:
            pre_l2.next = l1

        if origin_l1.val < origin_l2.val:
            return origin_l1
        return origin_l2

# @lc code=end
