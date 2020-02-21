# Given a linked list, determine if it has a cycle in it.
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
# If pos is -1, then there is no cycle in the linked list.

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Two Pointers
# time complexity: O(N), where N is the number of nodes in the given list.
# space complexity: O(1), the space used by slow and fast.
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            fast = head.next.next
            slow = head.next

            while fast != slow:
                fast = fast.next.next
                slow = slow.next
            return True
        
        except:
            return False
