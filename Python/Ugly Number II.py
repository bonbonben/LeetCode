# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.

# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        stack=[]
        heapq.heappush(stack, 1)
        nums = []
        seen = set()
        for i in range(1690):
            curMin = heapq.heappop(stack)
            nums.append(curMin)
            for mul in [2, 3, 5]:
                tmp = mul * curMin
                if tmp not in seen:
                    seen.add(tmp)
                    heapq.heappush(stack, tmp)
        return nums[n-1]
