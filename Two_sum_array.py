# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.


# bruteforce
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            for j in nums:
                if i + j == target and i != j:
                    return [nums.index(i), nums.index(j)]


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 12))  # [0,1]


# soritng


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i, num in enumerate(nums):
            a.append([num, i])
        a.sort()
        print(a)
        i, j = 0, len(nums) - 1
        while i < j:
            cur = a[i][0] + a[j][0]

            if cur == target:
                return [a[i][1], a[j][1]]
            elif cur < target:
                i += 1
            else:
                j -= 1


sol = Solution()
print(sol.twoSum([2, 11, 7, 15], 13))  # [0,1]


# hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            print(i, n)
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # [0, 1]
