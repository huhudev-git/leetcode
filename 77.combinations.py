#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        回溯法
        """
        result = []
        item = []
        self.gen(n, k, 0, item, result)
        return result

    def gen(self, n, k, num, item, result):
        if num == k:
            result.append(list(item))
            return

        for i in range(1, n+1):
            if not item or item[-1] < i:
                item.append(i)
                self.gen(n, k, num+1, item, result)
                item.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        通过 indices 选择，k 表示一次选择 k 个下标
        然后每次增加 indices 的值， 如果增加indices[i]， 则indices[i+1:k]都要增加
        """
        result = []
        # 使用元素
        pool = [i for i in range(1, n + 1)]
        if k > n:
            return

        # 下标
        indices = [i for i in range(k)]
        # 初始一个元素
        result.append([pool[i] for i in indices])

        while True:
            for i in reversed(range(k)):
                if indices[i] != i + n - k:
                    break  # 可以理解为goto
            else:
                return result

            indices[i] += 1  # goto 到这个位置
            for j in range(i+1, k):
                indices[j] = indices[j-1] + 1
            result.append([pool[i] for i in indices])


if __name__ == "__main__":
    s = Solution()
    print(s.combine(4, 2))
# @lc code=end
