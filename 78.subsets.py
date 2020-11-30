#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = [[]]
        # 100000
        # 000000
        # 110000
        # 010000

        for index in range(len(nums)):
            for j in range(len(res)):
                # copy list
                curr = list(res[j])
                curr.append(nums[index])
                res.append(curr)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))
# @lc code=end
