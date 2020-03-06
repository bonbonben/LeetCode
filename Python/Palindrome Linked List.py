# Given a singly linked list, determine if it is a palindrome.

# Input: 1->2
# Output: false

# Input: 1->2->2->1
# Output: true

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        mid = Solution.reverseList(Solution.findMidPoint(head))
        while mid:
            if mid.val != head.val:
                return False
            head, mid = head.next, mid.next
        return True
    
    def findMidPoint(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next if fast else slow
    
    def reverseList(head):
        left = None
        while head:
            right = head.next
            head.next = left
            left = head
            head = right
        return left
