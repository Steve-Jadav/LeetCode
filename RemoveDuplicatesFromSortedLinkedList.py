# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        current = head.next
        previous = head
        
        while current:
            if current.val != previous.val:
                previous.next = current
                previous = previous.next
            
            current = current.next
            
        previous.next = None
        return head
