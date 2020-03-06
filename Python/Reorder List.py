# Given a singly linked list L: L0→L1→…→Ln-1→Ln, reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        fast = head2.next
        head2.next = None
        # reverse mid->end to end->mid
        while fast:
            temp = fast.next
            fast.next = head2
            head2 = fast
            fast = temp
        slow, fast = head, head2
        # merge
        while slow:
            temp = slow.next
            slow.next = fast
            slow = slow.next
            fast = temp
