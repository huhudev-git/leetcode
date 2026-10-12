#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        # 贡献法：不枚举子数组，而是对每个元素 arr[i] 求
        # "它是几个子数组的最小值"，贡献 = arr[i] * 个数，最后求和。
        # 个数 = 左端点的选法 left[i] * 右端点的选法 right[i]。

        # 单调栈，存 (值, 该值能覆盖的长度)，从栈底到栈顶值递增
        stack = []
        # left[i]：从 i 往左，连续有几个元素能和 arr[i] 组成以它为最小值的子数组（含自己）
        left = [0] * len(arr)
        # right[i]：从 i 往右，同理
        right = [0] * len(arr)

        # 第一遍：从左往右算 left
        for i in range(len(arr)):
            count = 1  # 只包含自己
            # 栈顶比 arr[i] 大，挡不住 arr[i]，弹出并继承它覆盖的长度
            # （它覆盖的元素都比它大，自然也比 arr[i] 大，不用再逐个检查）
            # 用 > ：遇到相等的值就停，子数组归左边那个相等元素
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            left[i] = count
            stack.append((arr[i], count))

        stack.clear()

        # 第二遍：从右往左算 right，逻辑同上
        for i in range(len(arr) - 1, -1, -1):
            count = 1
            # 用 >= ：右边相等的值可以越过，和左边的 > 配合，
            # 保证有重复值时每个子数组只算给最左边的那个最小值，不重不漏
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            right[i] = count
            stack.append((arr[i], count))

        # 累加每个元素的贡献：值 × 左端点选法 × 右端点选法
        result = 0
        for i in range(len(arr)):
            result += arr[i] * left[i] * right[i]

        # Python 整数不会溢出，最后取一次模即可；其他语言需要在循环里取模
        return result % (10**9 + 7)

# @lc code=end
