# Problem 23
# Approach: Merge 2 linked lists (k-1) times
# Complexity: O(kN)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        
        current = lists[0]
        for i in range(0, len(lists) - 1):
            l1 = current
            l2 = lists[i + 1]
            current = self.merge(l1, l2)
        
        return current
        
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = dummyNode = ListNode(-1)
        
        while l1 and l2:
            if l1.val <= l2.val:
                dummyNode.next = ListNode(l1.val)
                l1 = l1.next
            else:
                dummyNode.next = ListNode(l2.val)
                l2 = l2.next
            dummyNode = dummyNode.next
            
        dummyNode.next = l1 or l2
        
        return head.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = point = ListNode(-1)
        q = PriorityQueue()
        
        for l in lists:
            if l:
                q.put((l.val, l))
        
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
                
        return head.next
