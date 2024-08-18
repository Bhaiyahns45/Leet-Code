
''''
1679. Max Number of K-Sum Pairs

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
