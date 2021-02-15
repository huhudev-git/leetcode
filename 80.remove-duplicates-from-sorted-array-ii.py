#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 3:
            return length

        count = 1
        index = 1

        for i in range(1, length):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count < 3:
                nums[index] = nums[i]
                index += 1

        return index


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 1, 1]))
# @lc code=end
