import numpy as np


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        if sorted(nums) == nums:
            return 0

        a = nums
        a = np.array((a))
        sorted_index = np.argsort(a)

        for i in range(len(a)):
            if sorted_index[i] != i:
                st = i
                break

        for i in range(len(a) - 1, 0, -1):
            if sorted_index[i] != i:
                ed = i
                break

        return ed - st + 1
