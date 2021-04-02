#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
from typing import List
import itertools


class Solution:

    def get_ip(self, s, a, b, c):
        v1 = a
        v2 = v1 + b
        v3 = v2 + c
        item = [s[:v1], s[v1:v2], s[v2:v3], s[v3:]]
        for i in item:
            if i.startswith("0") and len(i) != 1:
                return
            if int(i) > 255:
                return
        return '.'.join(item)

    def restoreIpAddresses(self, s: str) -> List[str]:
        table = {
            4: [[1, 1, 1, 1]],
            5: [[1, 1, 1, 2]],
            6: [[1, 1, 1, 3], [1, 1, 2, 2]],
            7: [[1, 1, 2, 3], [1, 2, 2, 2]],
            8: [[1, 1, 3, 3], [1, 2, 2, 3], [2, 2, 2, 2]],
            9: [[1, 2, 3, 3], [2, 2, 2, 3]],
            10: [[1, 3, 3, 3], [2, 2, 3, 3]],
            11: [[2, 3, 3, 3]],
            12: [[3, 3, 3, 3]],
        }

        length = len(s)
        if length not in table:
            return []

        ts = table[length]
        result = []

        for t in ts:
            for i in set(itertools.permutations(t, 4)):
                ip = self.get_ip(s, i[0], i[1], i[2])
                if ip:
                    result.append(ip)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.restoreIpAddresses("19216811"))


# @lc code=end
