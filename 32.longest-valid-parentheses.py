#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0

        stack = []
        stack.append(-1)
        max_len = 0

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()

                # if empty
                # mean meet )
                if not stack:
                    stack.append(i)

                length = i - stack[-1]
                if length > max_len:
                    max_len = length

        return max_len


# if __name__ == "__main__":
#     s = Solution()
#     print(s.longestValidParentheses("(()"))
#     print(s.longestValidParentheses("(()()"))
#     print(s.longestValidParentheses("(())()())"))
#     print(s.longestValidParentheses("()()()"))
#     print(s.longestValidParentheses("))(()())"))
#     print(s.longestValidParentheses("()(()"))
# @lc code=end
