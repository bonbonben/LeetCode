# Given a collection of intervals, merge all overlapping intervals.

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Sort
# time complexity: O(n log n)
# the runtime is dominated by the O(nlgn) complexity of sorting.
# space complexity: O(1) (or O(n))
# If we can sort intervals in place, we do not need more than constant additional space.
# Otherwise, we must allocate linear space to store a copy of intervals and sort that.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
