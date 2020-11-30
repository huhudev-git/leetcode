#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        converter = {
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "0":0,
        }

        num1 = list(map(lambda x: converter[x], num1))
        num2 = list(map(lambda x: converter[x], num2))
        length1 = len(num1) 
        length2 = len(num2)
        length = length1+length2

        result = [0 for _ in range(length)]

        for i1 in range(length1):
            for i2 in range(length2):
                offect = i1+i2+1
                result[offect] += num1[i1]*num2[i2]

        for i in range(length - 1, 0, -1):
            up = result[i] // 10
            result[i - 1] += up
            result[i] = result[i] % 10
        
        result = "".join(map(str, result))
        index = 0
        while index < length and result[index] == "0":
            index += 1
        if index == length:
            return "0"
        return result[index:]
        

if __name__ == "__main__":
    s=Solution()
    print(s.multiply("244", "0"))

# @lc code=end

