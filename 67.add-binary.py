#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        if len_a < len_b:
            a, b = b, a
            len_a, len_b = len_b, len_a

        offset = len_a - len_b
        up = False
        result = ""
        for i in range(len_b - 1, -1, -1):
            r = 0
            if a[offset + i] == "1":
                r += 1
            if b[i] == "1":
                r += 1
            if up:
                r += 1

            # print(i, r, a[offset + i], b[i])
            up = r > 1
            result = f"{r % 2}{result}"

        # print(result, up)

        for i in range(len_a - len_b - 1, -1, -1):
            if up:
                if a[i] == "1":
                    result = f"0{result}"
                else:
                    result = f"1{result}"
                    up = False
                continue
            result = f"{a[i]}{result}"

        if up:
            return f"1{result}"
        return result

    def addBinary(self, a: str, b: str) -> str:
        index = 0
        result = ""
        up = False

        na = len(a) - 1
        nb = len(b) - 1

        while na >= 0 or nb >= 0:
            r = 0
            if na >= 0:
                r += a[na] == "1"
            if nb >= 0:
                r += b[nb] == "1"
            r += up
            up = r > 1
            result = f"{r % 2}{result}"

            na -= 1
            nb -= 1
        if up:
            return f"1{result}"
        return result


# if __name__ == "__main__":
#     s = Solution()
#     print(s.addBinary("101111", "10"))

# @lc code=end
