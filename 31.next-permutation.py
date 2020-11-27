#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index, length = None, len(nums)
        for i in range(length - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                index = i - 1
                break

        if index is None:
            nums.reverse()
            return

        for i in range(length - 1, index, -1):
            if nums[index] < nums[i]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        index += 1
        j = length - 1

        # 转置剩余字串
        while index < j:
            nums[index], nums[j] = nums[j], nums[index]
            index += 1
            j -= 1

# @lc code=end
