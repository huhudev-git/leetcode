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

    def countSmaller(self, nums: List[int]) -> List[int]:
        # 归并排序：合并左右两半时，右半边的元素原本都在左半边元素的右边。
        # 左半边的元素 x 放进结果前，右半边已经放进去的元素都比 x 小，
        # 它们就是 x 右边比它小的数，个数直接加到 x 的答案上。
        counts = [0] * len(nums)

        # 排序的是下标而不是值，这样排序后还能知道每个值原来在哪个位置
        def sort(idx: List[int]) -> List[int]:
            if len(idx) <= 1:
                return idx

            mid = len(idx) // 2
            left = sort(idx[:mid])
            right = sort(idx[mid:])

            merged = []
            j = 0  # right 中已经放进 merged 的个数
            for i in left:
                # 右半边比 nums[i] 小的先放；相等的不算"更小"，所以用 <
                while j < len(right) and nums[right[j]] < nums[i]:
                    merged.append(right[j])
                    j += 1
                # right[0:j] 都比 nums[i] 小，且原来都在 i 的右边
                counts[i] += j
                merged.append(i)
            merged.extend(right[j:])
            return merged

        sort(list(range(len(nums))))
        return counts


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
