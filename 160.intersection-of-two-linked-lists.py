#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (headA is None) or (headA is None):
            return None

        tA = headA
        tB = headB

        # get A length
        lenA = 1
        while tA is not None:
            tA = tA.next
            lenA += 1

        # get B length
        lenB = 1
        while tB is not None:
            tB = tB.next
            lenB += 1

        # move to same length
        #   0 - |0 - 0
        #       ^     \
        #              0 - 0 - 0
        #             /
        #        0 - 0
        if lenB > lenA:
            for _ in range(lenB - lenA):
                headB = headB.next
        elif lenA > lenB:
            for _ in range(lenA - lenB):
                headA = headA.next

        # move both
        for _ in range(min(lenB, lenA)):
            if headA == headB:
                return headA
            headB = headB.next
            headA = headA.next

        return None

# @lc code=end
