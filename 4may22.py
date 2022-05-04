
''''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.


ex-1

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.


ex-2


Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.


'''

nums = [3,1,3,4,3]


k = 6


nums.sort()
left = 0
right = len(nums) - 1
ans = 0
while left < right:
    cur = nums[left] + nums[right]
    if cur == k:
        ans += 1
        left += 1
        right -= 1
    elif cur < k:
        left += 1
    else:
        right -= 1


print(ans)
