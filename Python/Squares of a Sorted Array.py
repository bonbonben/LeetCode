# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Sort
# time complexity: O(N log N), where N is the length of A.
# space complexity: O(N).
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(x*x for x in A)
