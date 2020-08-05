"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
# Problem 430

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head == None:
            return head
        
        current: Node = head
        
        while current:
            if current.child == None:
                current = current.next
                continue
            
            temp: Node = current.child
            
            while temp.next:
                temp = temp.next
            temp.next = current.next
            
            if current.next: 
                current.next.prev = temp
            
            current.next = current.child
            current.child.prev = current
            current.child = None
        
        return head
