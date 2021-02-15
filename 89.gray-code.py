#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def bin2gray(self, n):
        return (n >> 1) ^ n

    def gray2bin(self, n):
        mask = n >> 1
        while mask != 0:
            num = num ^ mask
            mask >>= 1

    def grayCode(self, n: int) -> List[int]:
        return [self.bin2gray(i) for i in range(2 ** n)]

# @lc code=end
