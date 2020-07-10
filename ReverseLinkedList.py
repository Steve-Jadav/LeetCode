# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        current = head.next
        previous = head
        previous.next = None
        
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        
        head = previous
        return head


# Recursive Approach:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if (head == None or head.next == None):
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
