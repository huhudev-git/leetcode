#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        before = ListNode()
        # a temp head
        result = before
        before.next = head

        while head:
            start = head
            end = head

            for _ in range(k-1):
                end = end.next
                if not end:
                    return result.next

            # connect pre node
            before.next = end
            # end.next is next head
            before = start

            # end.next is next head
            head = end.next

            end = end.next
            while start != head:
                # print(start.val, end.val)

                # start -> start_next
                start_next = start.next
                # start -> end.next
                start.next = end

                end = start
                start = start_next

        return result.next


# if __name__ == "__main__":
#     s = Solution()
#     h = s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)

# @lc code=end
