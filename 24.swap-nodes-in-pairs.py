#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        before = ListNode()
        # a temp head
        result = before
        before.next = head

        while head:
            first = head
            second = head.next
            if second:
                # first -> second -> head
                head = second.next

                # before -> second -> first
                before.next = second
                second.next = first
                first.next = head

                before = first
            else:
                break

        return result.next


# if __name__ == "__main__":
#     s = Solution()
#     h = s.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
#     while h:
#         print(h.val)
#         h = h.next

# @lc code=end
