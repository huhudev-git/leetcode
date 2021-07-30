#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
class Solution:

    lt_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",  "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

    def helper(self, n):
        if n == 0:
            return ""
        elif n < 20:
            return self.lt_20[n] + " "
        elif n < 100:
            return self.tens[n // 10] + " " + self.helper(n % 10)
        else:
            return self.lt_20[n // 100] + " Hundred " + self.helper(n % 100)

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ans = ""
        i = 0
        while num > 0:
            if num % 1000 != 0 or num >= 1000:
                temp_ans = self.helper(num % 1000)
                if temp_ans:
                    ans = temp_ans + self.thousands[i] + " " + ans
                else:
                    ans = temp_ans + ans

                i += 1
                num //= 1000
        return ans.strip()

# @lc code=end
