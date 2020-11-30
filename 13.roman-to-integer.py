#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        length = len(s)

        i = 0
        result = 0
        while i < length:
            c1 = table[s[i]]
            if i < length - 1:
                c2 = table[s[i + 1]]
                if c2 > c1:
                    result += (c2 - c1)
                    i += 2
                    continue
            result += c1
            i += 1
        return result


# if __name__ == "__main__":
#     s = Solution()
#     print(s.romanToInt("IV"))


# @lc code=end
