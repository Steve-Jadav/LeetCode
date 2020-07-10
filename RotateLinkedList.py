# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if head == None or head.next == None or k <= 0:
            return head
        
        length = self.getLengthOfList(head)
        if k % length == 0:
            return head
        
        # Find the nth element from the end
        n = (k % length) + 1
        slow = head
        fast = head
        
        for _ in range(n-1):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        newHead = slow.next
        slow.next = None
        fast.next = head
        
        return newHead
    
    def getLengthOfList(self, head: ListNode) -> int:
        temp = head
        n = 0
        
        while temp:
            n += 1
            temp = temp.next
        
        return n
