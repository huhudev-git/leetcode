#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num

        if k >= len(num):
            return "0"

        result = []

        for i in range(len(num)):
            while result and result[-1] > num[i] and k > 0:
                result.pop()
                k -= 1
            if (num[i] != "0") or result:
                result.append(num[i])

        # left k
        while result and k:
            result.pop()
            k -= 1

        if result:
            return ''.join(result)
        return "0"


if __name__ == "__main__":
    s = Solution()
    print(s.removeKdigits("4321", 2))

# @lc code=end
