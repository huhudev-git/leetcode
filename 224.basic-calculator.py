#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:

    def _op(self, a, b, op):
        print(a, op, b)
        if op == "-":
            return int(a) - int(b)
        else:
            return int(a) + int(b)

    def calculate(self, s: str) -> int:
        data = []
        ops = []

        sum_ = 0
        i = 0
        ok = False
        while i < len(s):
            off = 1
            while True:
                str_ = s[i:i+off]
                if str_.isdigit():
                    off += 1
                    if i+off >= len(s):
                        i += off
                        break
                else:
                    i += off
                    break

            if str_ == " ":
                continue

            print("-", str_, ok)

            if str_.isdigit():
                print(str_, ok)
                if ok:
                    if data:
                        sum_ += self._op(data.pop(), str_, ops.pop())
                    else:
                        sum_ = self._op(sum_, str_, ops.pop())
                    ok = False
                else:
                    data.append(str_)

            else:
                if str_ == "(":
                    ok = False
                elif str_ == ")":
                    ok = True
                else:
                    ops.append(str_)
                    ok = True

        while data:
            b = data.pop()
            if data:
                a = data.pop()
                sum_ += self._op(a, b, ops.pop())
            else:
                if ops:
                    sum_ += self._op(sum_, b, ops.pop())
                else:
                    sum_ = b

        return sum_


if __name__ == "__main__":
    s = Solution()
    print(s.calculate("1 + 1"))

# @lc code=end
