# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result = 0
        resultList = ListNode()
        
        tempNode = l1
        i = 0
        
        while (tempNode):
            result += tempNode.val * (pow(10, i))
            i += 1
            tempNode = tempNode.next
            
        tempNode = l2
        i = 0
        
        while (tempNode):
            result += tempNode.val * (pow(10, i))
            i += 1
            tempNode = tempNode.next
        
        node = ListNode()
        tempNode = node
        
        while (result):
            value = result % 10
            result = int(result//10)
            node.val = value
            if (result != 0):
                node.next = ListNode()
                node = node.next
            
        return tempNode
