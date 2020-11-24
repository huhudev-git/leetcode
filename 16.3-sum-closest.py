#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = 10E4
        min_gap = 10E4
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                gap = abs(sum3 - target)
                if gap < min_gap:
                    min_gap = gap
                    result = sum3
                if sum3 > target:
                    right -= 1
                elif sum3 < target:
                    left += 1
                else:
                    return target
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([0, 0, 0], 1))
# @lc code=end
