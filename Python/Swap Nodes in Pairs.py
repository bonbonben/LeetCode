# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head        
        tmp = dummy
        while tmp.next:
            if not tmp.next.next:
                return dummy.next
            else:
                t1 = tmp.next
                t2 = tmp.next.next
                t3=tmp.next.next.next
                tmp.next=t2
                tmp.next.next=t1
                tmp.next.next.next=t3
                tmp=tmp.next.next
        return dummy.next
