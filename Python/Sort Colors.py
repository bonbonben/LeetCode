# Given an array with n objects colored red, white or blue.
# Sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rightmost0 = 0
        leftmost2 = len(nums) - 1
        p = 0
        while p <= leftmost2:
            if nums[p] == 0:
                nums[rightmost0], nums[p] = nums[p], nums[rightmost0]
                rightmost0 += 1
                p += 1
            elif nums[p] == 2:
                nums[leftmost2], nums[p] = nums[p], nums[leftmost2]
                leftmost2 -= 1
            else:
                p += 1
