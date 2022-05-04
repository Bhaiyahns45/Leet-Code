
''''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
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