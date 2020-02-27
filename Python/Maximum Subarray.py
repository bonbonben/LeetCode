# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        #print(maxsum)
        maxtillnow = 0
        for i in nums:
            maxtillnow += i
            if maxtillnow >= maxsum:
                maxsum = maxtillnow
            if maxtillnow < 0:
                maxtillnow = 0
            #print(maxtillnow, maxsum)
        return maxsum
