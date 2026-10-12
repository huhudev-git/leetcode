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

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child = 0
        cookie = 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1

        return child

# @lc code=end
