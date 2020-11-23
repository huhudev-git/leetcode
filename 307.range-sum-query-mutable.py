#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start
from typing import List


class SegmentTree():

    def __init__(self, nums: List[int]):
        self.length = len(nums)
        self.data = [0] * self.length * 4
        self.nums = nums

        self.build(0, 0, self.length-1)

    # O(n)
    def build(self, index, left, right):
        if left == right:
            self.data[index] = self.nums[left]
            return

        mid = (left + right) // 2
        self.build(index*2 + 1, left, mid)
        self.build(index*2 + 2, mid+1, right)
        self.data[index] = self.data[index * 2 + 1] + self.data[index * 2 + 2]

    # O(logn)
    def update(self, index: int, val: int, pos, left, right) -> None:
        if left == right and left == index:
            self.data[pos] = val
            return

        mid = (left + right) // 2
        if index <= mid:
            self.update(index, val, pos * 2 + 1, left, mid)
        else:
            self.update(index, val, pos * 2 + 2, mid+1, right)

        self.data[pos] = self.data[pos * 2 + 1] + self.data[pos * 2 + 2]

    # O(logn + k)
    def sumRange(self, qleft, qright, left, right, pos) -> int:
        if qleft > right or qright < left:
            return 0
        if qleft <= left and qright >= right:
            return self.data[pos]

        mid = (left+right) // 2
        return self.sumRange(qleft, qright, left, mid, pos*2 + 1) + \
            self.sumRange(qleft, qright, mid + 1, right, pos*2 + 2)


class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.tree = SegmentTree(nums)

    def update(self, i: int, val: int) -> None:
        self.tree.update(i, val, 0, 0, self.tree.length - 1)

    def sumRange(self, i: int, j: int) -> int:
        return self.tree.sumRange(i, j, 0, self.tree.length - 1, 0)


if __name__ == "__main__":
    n = NumArray([1, 3, 5])
    print(n.sumRange(0, 2))
    n.update(1, 2)
    print(n.sumRange(0, 2))

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

# @lc code=end
