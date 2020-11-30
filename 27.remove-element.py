#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        index = 0
        for i in range(length):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index


# if __name__ == "__main__":
#     s = Solution()
#     print(s.removeElement([3, 2, 2, 3], 3))

# @lc code=end
