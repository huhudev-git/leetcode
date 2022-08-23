#
# @lc app=leetcode id=1003 lang=python3
#
# [1003] Check If Word Is Valid After Substitutions
#

# @lc code=start
class Solution:
    # def isValid(self, s: str) -> bool:
    #     while True:
    #         length = len(s)
    #         if length == 0:
    #             return True

    #         s = s.replace("abc", "")
    #         if len(s) == length:
    #             return False

    def isValid(self, s: str) -> bool:
        while True:
            length = len(s)

            if length == 0:
                return True

            flag = False
            for i in range(length):
                if self.check_abc(s, i, length):
                    s = s[:i] + s[i+3:]
                    flag = True
                    break

            if flag:
                continue

            return False

    def check_abc(self, s, i, length):
        if i + 2 >= length:
            return False

        if s[i] == 'a' and s[i+1] == 'b' and s[i+2] == 'c':
            return True


# @lc code=end
