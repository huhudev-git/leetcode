#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._min = []
        self._data = []

    def push(self, x: int) -> None:
        self._data.append(x)
        if (not self._min):
            self._min.append(x)
        else:
            if x > self._min[-1]:
                x = self._min[-1]
            self._min.append(x)

    def pop(self) -> None:
        # if not self._data:
        #     return

        self._data.pop()
        self._min.pop()

    def top(self) -> int:
        return self._data[-1]

    def getMin(self) -> int:
        return self._min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
