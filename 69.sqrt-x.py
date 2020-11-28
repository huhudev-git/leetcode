#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        """
        https://blog.csdn.net/chenrenxiang/article/details/78286599#:~:text=https%3A%2F%2Fblog.csdn.net%2Fu013053957%2Farticle%2F,%E6%89%80%E9%9C%80%E7%9B%AE%E6%A0%87%E6%88%96%E7%BB%93%E6%9E%9C%E3%80%82\
        https://zhuanlan.zhihu.com/p/64728645
        """
        if x <= 1:
            return x
        root = x
        while abs(x - root ** 2) > 0.000001:
            root = (x / root + root) / 2
        return int(root)


# if __name__ == "__main__":
#     s = Solution()
#     print(s.mySqrt(8))
# @lc code=end
