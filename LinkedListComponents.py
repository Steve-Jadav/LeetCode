# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# +++++++++++++++
# Problem 817
# +++++++++++++++

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        if head == None:
            return 0
        
        graph = set(G)
        components = 0
        flag = False
        
        while head:
            if head.val in graph:
                flag = True
                
            if flag == True and head.val not in graph:
                components += 1
                flag = False
            
            if head.next == None and flag == True:
                components += 1
                
            head = head.next
        
        return components
