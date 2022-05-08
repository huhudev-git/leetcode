#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}

        for i, num in enumerate(nums):
            if num not in table:
                table[num] = [i]
            else:
                table[num].append(i)

        for num, indexs in table.items():
            if len(indexs) >= 2:
                for i, j in zip(indexs[:-1], indexs[1:]):
                    if j - i <= k:
                        return True
        return False
# @lc code=end
