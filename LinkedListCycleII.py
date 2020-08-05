# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Problem 142

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        hashset = set()
        tempNode = head
        
        while tempNode:
            if tempNode in hashset:
                return tempNode
            hashset.add(tempNode)
            tempNode = tempNode.next
        
        return None






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        # Detect if there is a cycle
        slow = head
        fast = head.next
        
        while slow != fast:
            if fast == None or fast.next == None:
                return None
            slow = slow.next
            fast = fast.next.next
        
        # Find the length of the cycle
        length = 1
        fast = slow.next
        
        while fast != slow:
            fast = fast.next
            length += 1 
        
        # Move forward length times
        fast = head
        slow = head
        
        for i in range(length):
            fast = fast.next
            
        while fast != slow:
            slow = slow.next
            fast = fast.next
        
        return slow
