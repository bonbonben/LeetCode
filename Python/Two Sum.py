# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Given nums = [2, 7, 11, 15], target = 9, return [0, 1].

# Two for loop
#class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        res = {}
#        result = []
#        i = 0
#        while i < len(nums):
#            j = i + 1
#            while j < len(nums):
#                if nums[i] + nums[j] == target:
#                    result = [i,j]
#                j += 1
#            i += 1
#        return result

# Sort
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        result = []
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    result = [i,j]
                j += 1
            i += 1
        return result
