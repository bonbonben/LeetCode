# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# Return a deep copy of the list.
# The Linked List is represented in the input/output as a list of n nodes.
# Each node is represented as a pair of [val, random_index] where:
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        copies = {None: None}
        n = head
        while n:
            for node in [n, n.next, n.random]:
                if node not in copies:
                    copies[node] = Node(node.val)
            copies[n].next = copies[n.next]
            copies[n].random = copies[n.random]
            n = n.next
        return copies[head]
