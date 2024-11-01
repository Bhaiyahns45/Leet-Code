
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j
    


print(removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))


class Solution:

    @staticmethod
    def findLastOccurrenceRecursive(nums: List[int], key: int, first: int, last: int) -> int:
        # Performs a modified binary search to find the last occurrence of 'key' in the array 'nums'
        mid = (first + last) // 2

        if nums[mid] == key:
            if mid + 1 >= len(nums) or nums[mid + 1] != key:
                return mid
            return Solution.findLastOccurrenceRecursive(nums, key, mid + 1, last)

        return Solution.findLastOccurrenceRecursive(nums, key, first, mid - 1)

    @staticmethod
    def findLastOccurrenceIterative(nums: List[int], key: int, first: int, last: int) -> int:
        # Performs an iterative binary search to find the last occurrence of 'key' in the array 'nums'
        while first <= last:
            mid = (first + last) // 2

            if nums[mid] == key:
                if mid + 1 >= len(nums) or nums[mid + 1] != key:
                    return mid
                first = mid + 1
            else:
                last = mid - 1

        return first - 1

    def removeDuplicates(self, nums: List[int]) -> int:
        write_index = 0
        read_index = 0

        while read_index < len(nums):
            # Find the last occurrence of the current element using binary search
            read_index = self.findLastOccurrenceIterative(nums, nums[read_index], read_index + 1, len(nums) - 1)

            # Write the unique element to the current position tracked by 'write_index'
            nums[write_index] = nums[read_index]
            write_index += 1
            read_index += 1

        return write_index