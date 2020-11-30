#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#

# @lc code=start
from typing import List


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 4:
            return False

        L = sum(nums)
        if L % 4 != 0:
            return False

        d = L // 4

        nums = sorted(nums, reverse=True)
        bucket = [0, 0, 0, 0]
        return self.gen(0, nums, d, bucket)

    def gen(self, index, nums, target, bucket):
        if index >= len(nums):
            for b in bucket:
                if b != target:
                    return False
            return True

        for i in range(4):
            if bucket[i] + nums[index] > target:
                continue

            # put nums[index] in this bucket[i]
            bucket[i] += nums[index]

            # put next num in bucket
            if self.gen(index + 1, nums, target, bucket):
                return True

            # if reach here mean no solution when put nums[index] in this bucket[i]
            # so not put here
            bucket[i] -= nums[index]
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]))
# @lc code=end
