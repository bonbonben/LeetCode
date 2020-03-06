# Reverse a singly linked list.

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if(head == None or head.next == None):
            return head
        list_to_do = head.next
        reversed_list = head
        reversed_list.next = None
        
        while(list_to_do != None):
            temp = list_to_do
            list_to_do = list_to_do.next
            temp.next = reversed_list
            reversed_list = temp
        
        return reversed_list
