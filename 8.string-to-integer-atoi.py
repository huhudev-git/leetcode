#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:

        num = False
        word = False
        flag = False
        pre_flag = False
        result = []

        for i in s:
            if i.isdigit():
                if word:
                    break

                if pre_flag:
                    flag = True

                result.append(i)
                num = True
            elif num:
                break
            elif i == "-" or i == "+":
                if pre_flag:
                    return 0
                pre_flag = i
            elif i == " ":
                if pre_flag:
                    return 0
                continue
            else:
                word = True

        if not result:
            return 0

        result = ''.join(result)
        result = int(result)
        if result >= 1 << 31:
            result = 1 << 31

            if (not flag) or (pre_flag != "-"):
                return result - 1

        if flag and pre_flag == "-":
            result = -result

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("42"))

# @lc code=end
