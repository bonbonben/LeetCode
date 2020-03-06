# Sort a linked list in O(n log n) time using constant space complexity.

# Input: 4->2->1->3
# Output: 1->2->3->4

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # merge and sort
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        # divide into two parts
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # slow.next should be head of second part
        secondHead = slow.next
        slow.next = None
        # divide left and right part
        left = self.sortList(head)
        right = self.sortList(secondHead)
        # merge the sorted list
        return self.merge(left, right)
    
    def merge(self, left, right):
        dummy = ListNode(0)
        temp = dummy
        while left and right:
            if left.val <= right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
    
        if left:
            temp.next = left
        else:
            temp.next = right
    
        return dummy.next
