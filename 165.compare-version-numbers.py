#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        v1, v2 = zip(*zip_longest(v1, v2, fillvalue=0))
        return [0, 1, -1][(v1 > v2) - (v1 < v2)]

    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        length1 = len(v1)
        length2 = len(v2)

        if length1 > length2:
            length = length2
            last = v1
            result = 1
        elif length1 < length2:
            length = length1
            last = v2
            result = -1
        else:
            length = length1
            last = []
            result = 0

        for i in range(length):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1

        for i in last[length:]:
            if int(i) != 0:
                return result
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.compareVersion('1.0', '1.0'))
# @lc code=end
