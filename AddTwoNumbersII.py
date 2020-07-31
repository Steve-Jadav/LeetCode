# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number1, number2 = 0, 0
        
        while l1:
            number1 = (number1 * 10) + l1.val
            l1 = l1.next
        
        while l2:
            number2 = (number2 * 10) + l2.val
            l2 = l2.next
            
        total = number1 + number2
        
        if total == 0:
            return ListNode(0)
        
        node, prev = None, None
        
        # Insert at the beginning of the list
        while total > 0:
            digit = total % 10
            node = ListNode(digit)
            if prev != None:
                node.next = prev
            prev = node
            total = int(total // 10)
            
        return node
