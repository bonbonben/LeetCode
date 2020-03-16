# Given a binary tree, determine if it is a valid binary search tree (BST).
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Input: [2,1,3]
# Output: true

# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
max = sys.maxsize
min = -sys.maxsize - 1

class Solution:
    def isValidBST(self, root):
        return self.isVaild_helper(root, min, max)

    def isVaild_helper(self, root, minVal, maxVal):
        if root is None:
            return True
        if root.val >= maxVal or root.val <= minVal:
            return False
        return self.isVaild_helper(root.left, minVal, root.val) and self.isVaild_helper(root.right, root.val, maxVal)
