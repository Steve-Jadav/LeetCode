# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# ++++++++++++++
# Problem 19
# ++++++++++++++

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return None
        
        fast: ListNode = head
        slow: ListNode = head
        
        for i in range(n):
            fast = fast.next
        
        if fast == None:
            head = head.next
            return head
        
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
