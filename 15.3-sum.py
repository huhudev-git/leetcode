#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        result = []
        nums.sort()

        if nums[-1] == 0:
            if nums[0] == 0:
                return [[0, 0, 0]]
            else:
                return []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            a = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                # chance of nums[left] + nums[right] == -a is usually small than > or <
                if nums[left] + nums[right] > -a:
                    right -= 1
                elif nums[left] + nums[right] < -a:
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]])

                    # move duplicate
                    while (left < right and nums[left] == nums[left + 1]):
                        left += 1
                    # move duplicate
                    while (left < right and nums[right] == nums[right - 1]):
                        right -= 1

                    # move -> <-
                    left += 1
                    right -= 1

        return result


# if __name__ == "__main__":
#     s = Solution()
#     s.threeSum([0, 0, 0])
# @lc code=end
