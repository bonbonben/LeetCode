# There is a robot starting at position (0, 0), the origin, on a 2D plane.
# Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
# The move sequence is represented by a string, and the character moves[i] represents its ith move.
# Valid moves are R (right), L (left), U (up), and D (down).
# If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

# Input: "UD"
# Output: true

# Input: "LL"
# Output: false

# time complexity: O(N), where N is the length of moves. We iterate through the string.
# space complexity: O(1).
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1
        return x == y == 0
