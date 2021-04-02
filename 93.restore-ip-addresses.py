#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        length = len(s)
        result = []
        if length > 12:
            return result
        item = []
        self.gen(s, 1, item, result)

    def gen(self, index, item, result):

        # @lc code=end
