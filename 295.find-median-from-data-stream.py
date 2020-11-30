#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
from heapq import heappop, heappush, heapreplace


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 较大的一方
        self.min_heap = []
        # 较小的一方
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heappush(self.max_heap, -num)
            return

        # 两个堆元素数量相同
        if len(self.max_heap) == len(self.min_heap):
            if num < -self.max_heap[0]:
                heappush(self.max_heap, -num)
            else:
                heappush(self.min_heap, num)

        # 最大堆数量 > 最小堆数量
        elif len(self.max_heap) > len(self.min_heap):
            # 如果 数 > 最大堆的大 -> 放到最小堆
            if num > -self.max_heap[0]:
                heappush(self.min_heap, num)
            else:
                # 先把最大堆的最大放到最小堆
                # 然后数放进最大堆
                heappush(self.min_heap, -self.max_heap[0])
                heapreplace(self.max_heap, -num)

        elif len(self.max_heap) < len(self.min_heap):
            # 如果 数 < 最小堆的小 -> 放到最大堆
            if num < self.min_heap[0]:
                heappush(self.max_heap, -num)
            else:
                # 先把最小堆的最小放到最大堆
                # 然后数放进最小堆
                heappush(self.max_heap, -self.min_heap[0])
                heapreplace(self.min_heap, num)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
