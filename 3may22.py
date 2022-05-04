
'''

Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in 
ascending order, then the whole array will be sorted in ascending order.


ex-1

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

ex-2

Input: nums = [1,2,3,4]
Output: 0

'''

import numpy as np


## 1st approach

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
    
    
 ## 2nd approach
    
    
import numpy as np

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        
        if sorted(nums) == nums:
            return 0
        
        a=nums
        
        a = np.array((a))
        sorted_index = np.argsort(a)
                
        l , h = 0, len(a)-1

        for i in range(len(a)):
            if sorted_index[i] != i:
                l = max(l, sorted_index[i])
                h = min(h, sorted_index[i])
                
                
        return l-h+1
