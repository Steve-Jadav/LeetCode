# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None
        
        # If the elements are towards the head of the linked list.
        while head.val == val:
            head = head.next
            # Reached the end. Hence, the list has no other values than "val".
            if head == None:
                return None
        
        previous = head
        current = head
        
        while current:
            if current.val == val:
                previous.next = current.next
                current = current.next
                continue
            previous = current
            current = current.next
        
        return head
