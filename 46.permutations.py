#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        回溯法
        """
        result = []
        self.dfs(nums, 0, result)
        return result

    def dfs(self, nums, index, result):
        if index == len(nums):
            result.append(list(nums))
        else:
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                self.dfs(nums, index + 1, result)
                nums[i], nums[index] = nums[index], nums[i]
# @lc code=end
