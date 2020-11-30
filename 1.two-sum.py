#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        哈希表
        """
        table = {n: i for i, n in enumerate(nums)}
        for i, n in enumerate(nums):
            other = table.get(target - n, None)
            if other is not None and other != i:
                return [i, other]
# @lc code=end
