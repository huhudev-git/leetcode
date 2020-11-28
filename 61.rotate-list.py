#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        origin_head = head
        length = 0
        last = head
        while head:
            length += 1
            last = head
            head = head.next

        # save last
        end = last
        # get real k
        k = (length - k % length) % length
        if k == 0 or length == 1:
            return origin_head

        # move to k - 1
        head = origin_head
        for _ in range(k - 1):
            head = head.next

        # replace
        result_head = head.next
        head.next = None
        end.next = origin_head

        return result_head


# if __name__ == "__main__":
#     s = Solution()
#     # h = s.rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 5)
#     h = s.rotateRight(ListNode(1), 5)
#     while h:
#         print(h.val)
#         h = h.next

# @lc code=end
