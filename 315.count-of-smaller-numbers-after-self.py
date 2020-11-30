#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start
from typing import List


class Solution:
    # too slow
    def countSmaller(self, nums: List[int]) -> List[int]:
        return list(map(
            lambda n: len(list(filter(
                lambda x: nums[n] > x,
                nums[n:],
            ))),
            range(len(nums))),
        )

    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        bst = BinarySearchTree()
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = bst.insert(nums[i])
        return ans


class TreeNode(object):
    def __init__(self, val):
        self.leftCnt = 0
        self.val = val
        self.cnt = 1
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            return 0
        root = self.root
        cnt = 0
        while root:
            if val < root.val:
                root.leftCnt += 1
                if root.left is None:
                    root.left = TreeNode(val)
                    break
                root = root.left
            elif val > root.val:
                cnt += root.leftCnt + root.cnt
                if root.right is None:
                    root.right = TreeNode(val)
                    break
                root = root.right
            else:
                cnt += root.leftCnt
                root.cnt += 1
                break
        return cnt


if __name__ == "__main__":
    s = Solution()
    # print(s.countSmaller([5, 2, 6, 1]))
    print(s.countSmaller([2, 0, 1]))
# @lc code=end
