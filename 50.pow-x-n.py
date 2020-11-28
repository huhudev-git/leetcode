#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        flag = n < 0
        if flag:
            n = -n
        while n:
            if n % 2 != 0:
                result *= x
            x *= x
            n //= 2
        if flag:
            return 1 / result
        return result


if __name__ == "__main__":
    s = Solution()
    s.myPow(2.0, 10)
# @lc code=end
