#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        end = length - 1
        start = 0

        while start < end:
            s = numbers[start] + numbers[end]
            if s > target:
                end -= 1
            elif s < target:
                start += 1
            else:
                return [start + 1, end + 1]

# @lc code=end
