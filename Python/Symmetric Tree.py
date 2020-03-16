# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, [1,2,2,3,4,4,3] is symmetric
# But [1,2,2,null,3,null,3] is not

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return not root or self.is_same(root.left, root.right)
    
    def is_same(self, left, right):
        return left and right and left.val == right.val and self.is_same(left.left, right.right) and self.is_same(left.right, right.left) or left is right
