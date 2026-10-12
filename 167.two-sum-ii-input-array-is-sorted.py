#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        end = length - 1
        start = 0

        while start < end:
            s = numbers[start] + numbers[end]
            if s > target:
                end -= 1
            elif s < target:
                start += 1
            else:
                return [start + 1, end + 1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i1 in range(len(numbers)):
            find = target - numbers[i1]
            i2 = self.binsearch(find, numbers, i1)
            if i2 != -1:
                return [i1 + 1, i2 + 1]

    def binsearch(self, target: int, arr: List[int], start: int):
        end = len(arr)
        while start < end:
            mid = start + int((end - start) // 2)
            if arr[mid] > target:
                end = mid
            elif arr[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1

# @lc code=end
