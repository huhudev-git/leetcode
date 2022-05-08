#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
from typing import List


class Item():
    def __init__(self, char, num) -> None:
        self.char = char
        self.num = num


class Solution:
    def compress(self, chars: List[str]) -> int:
        left, right = 0, 0
        write = 0
        chars.append('-1')
        length = len(chars)

        while right < length:
            if chars[left] != chars[right]:

                if left + 1 == right:
                    chars[write] = chars[left]
                    left += 1
                    write += 1
                    continue
                else:
                    chars[write] = chars[left]
                    num = right - left

                    numbers = []
                    while num >= 10:
                        number = num % 10
                        numbers.append(number)
                        num = num // 10
                    numbers.append(num)

                    for i, n in enumerate(numbers[::-1]):
                        chars[write + 1 + i] = str(n)

                    left = right
                    write += 1 + len(numbers)

            right += 1

        for _ in range(length - write):
            chars.pop()
        return write


if __name__ == "__main__":
    s = Solution()
    print(s.compress(["a", "a", "b", "b", "c", "c", "c"]))

# @lc code=end
