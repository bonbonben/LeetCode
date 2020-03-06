# Given a singly linked list, group all odd nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.
# The program should run in O(1) space complexity and O(nodes) time complexity.
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...

# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odds = ListNode(0)
        evens = ListNode(0)
        oddsHead = odds
        evensHead = evens
        isOdd = True
        while head:
            if isOdd:
                odds.next = head
                odds = odds.next
            else:
                evens.next = head
                evens = evens.next
            isOdd = not isOdd
            head = head.next
        evens.next = None
        odds.next = evensHead.next
        return oddsHead.next
