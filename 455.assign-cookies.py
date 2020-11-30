#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s or not g:
            return 0

        s = sorted(s)
        g = sorted(g)

        g1 = 0
        s1 = 0

        while g1 < len(g) and s1 < len(s):
            if g[g1] <= s[s1]:
                g1 += 1
            s1 += 1
        return g1

# @lc code=end
