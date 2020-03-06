# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = ListNode(-1)
        previous = start
        while l1 and l2:
            if l1.val <= l2.val:
                previous.next = l1
                l1 = l1.next
            else:
                previous.next = l2
                l2 = l2.next
            previous = previous.next
        
        previous.next = l1 if l1 is not None else l2
        return start.next
