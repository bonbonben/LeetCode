# Given a binary tree, determine if it is height-balanced.
# A height-balanced binary tree: a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Given the following tree [3,9,20,null,null,15,7]: Return true.
# Given the following tree [1,2,2,3,3,null,null,4,4]: Return false.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self, root: TreeNode) -> int:
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))
