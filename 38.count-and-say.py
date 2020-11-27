#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        n -= 1

        for _ in range(n):
            index_c = s[0]
            num = 0
            new_s = ""

            for i in s:
                if i != index_c:
                    new_s += f"{num}{index_c}"
                    index_c = i
                    num = 1
                else:
                    num += 1

            s = f"{new_s}{num}{index_c}"
        return s


# if __name__ == "__main__":
#     s = Solution()
#     print(s.countAndSay(6))
# @lc code=end
