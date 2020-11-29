#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    # Time Limit Exceeded
    def minWindow(self, s: str, t: str) -> str:
        checker = {i: True for i in t}

        begin = 0
        length = len(s)
        min_ = ""

        while begin < length:
            while begin < length and (not checker.get(s[begin], False)):
                begin += 1

            temp_checker = {i: 0 for i in t}
            check_num = 0
            for i in t:
                temp_checker[i] += 1
                check_num += 1

            # print(begin)

            for i in range(begin, length):
                # print(temp_checker)
                if temp_checker.get(s[i], False):
                    temp_checker[s[i]] -= 1
                    check_num -= 1
                    if check_num == 0:
                        if not min_ or len(min_) > i - begin:
                            min_ = s[begin: i+1]
                        break
            begin += 1

        return min_

    def minWindow(self, s: str, t: str) -> str:
        """
        x a y z x z y
        ^   ^ ^
        x a y z x z y
            ^ ^ ^
        x a y z x z y
              ^ ^   ^
        """
        # for find first
        counter = {i: 0 for i in t}
        for i in range(len(t)):
            counter[t[i]] += 1

        # record all t char index
        table = {i: [] for i in t}
        for i in range(len(s)):
            if s[i] in counter:
                table[s[i]].append(i)

        first = []
        for k in table:
            while counter[k]:
                # if we cannot get first range
                if not table[k]:
                    return ""

                # remove from index table
                i = table[k].pop(0)
                first.append(i)
                counter[k] -= 1

        # get first range
        begin = min(first)
        end = max(first)
        result = s[begin: end + 1]

        # print(begin, end)
        # print(table)

        while True:
            # char at begin
            begin_c = s[begin]

            # no left begin char
            if not table[begin_c]:
                return result

            # update begin_c index
            temp = table[begin_c].pop(0)
            # if begin_c index > end -> update end
            if end < temp:
                end = temp

            # move begin to next char
            # move 1 first
            begin += 1
            while s[begin] not in table:
                begin += 1

            # if now begin - end < len()
            if len(result) > end - begin:
                result = s[begin: end + 1]


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("acbbaca", "aba"))
    # print(s.minWindow("a", "b"))
    # print(s.minWindow("ADOBECODEBANC", "ABC"))
    # print(s.minWindow("a", "aa"))
    # print(s.minWindow("bba", "ab"))
# @lc code=end
