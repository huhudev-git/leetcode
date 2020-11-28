#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        table = {0: 0, 1: 0, 2: 0}
        for n in nums:
            table[n] += 1

        index = 0
        for i in range(3):
            while table[i]:
                nums[index] = i
                table[i] -= 1
                index += 1

    def sortColors(self, nums: List[int]) -> None:
        length = len(nums)
        zero = -1
        one = 0
        two = length

        while one < two:
            if nums[one] == 1:
                one += 1
            elif nums[one] == 2:
                two -= 1
                nums[one], nums[two] = nums[two], nums[one]
            else:
                # if zero -> 1 than one -> 1
                zero += 1
                nums[one], nums[zero] = nums[zero], nums[one]
                one += 1

# @lc code=end
