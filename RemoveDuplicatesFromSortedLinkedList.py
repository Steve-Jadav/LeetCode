# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        start = head
        iterator = head
        
        while iterator:
            if start.val != iterator.val:
                start = start.next
                start.val = iterator.val
            iterator = iterator.next
        
        start.next = None
        return head
