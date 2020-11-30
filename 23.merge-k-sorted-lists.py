#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, a):
        return self.val == a.val

    def __lt__(self, a):
        return self.val < a.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        heap = []
        head = None
        lists = sorted(lists, key=lambda x: x.val if x else 0)
        length = len(lists)

        for i in range(length):
            # select first not None
            if not head and lists[i]:
                head = lists[i]
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))

        node = ListNode()
        while heap:
            min_node = heapq.heappop(heap)
            index = min_node[1]
            min_node = lists[index]
            # print(min_node.val, end="->")

            # link the node
            node.next = min_node
            node = min_node

            # this node move to next
            if node.next:
                lists[index] = lists[index].next
                heapq.heappush(heap, (node.next.val, index))
        return head


# if __name__ == "__main__":
    # s = Solution()
    # s.mergeKLists([
    #     ListNode(1, ListNode(4, ListNode(5))),
    #     ListNode(1, ListNode(3, ListNode(4))),
    #     ListNode(2, ListNode(6)),
    # ])

    # h = s.mergeKLists([
    #     ListNode(0, ListNode(1)),
    # ])
    # while h:
    #     print(h.val)
    #     h = h.next
# @lc code=end
