# Problem 82

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummyNode = ListNode(-1)
        dummyNode.next = head
        tempNode = dummyNode
        
        while tempNode.next != None and tempNode.next.next != None:
            if (tempNode.next.val == tempNode.next.next.val):
                duplicate = tempNode.next.val
                while (tempNode.next != None and tempNode.next.val == duplicate):
                    tempNode.next = tempNode.next.next
            
            else:
                tempNode = tempNode.next
        
        return dummyNode.next
