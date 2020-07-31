"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Problem 138
# Approach: Time O(n), Space: O(n)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if head == None:
            return head
        
        hashmap = dict()
        tempNode = head
        
        while tempNode:
            hashmap.update({ tempNode: Node(tempNode.val) })
            tempNode = tempNode.next
        
        tempNode = head

        while tempNode:
            if tempNode.next:
                hashmap[tempNode].next = hashmap[tempNode.next]
            if tempNode.random:
                hashmap[tempNode].random = hashmap[tempNode.random]
            tempNode = tempNode.next
        
        return hashmap[head]


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Approach: Time O(n), Space: O(1)
# Video Tutorial: https://www.youtube.com/watch?v=OvpKeraoxW0

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if head == None:
            return head
        
        tempNode = head
        # First pass
        while tempNode:
            nextNode = tempNode.next
            tempNode.next = Node(x = tempNode.val, next = nextNode)
            tempNode = nextNode
        
        tempNode = head
        # Second pass
        while tempNode:
            clone = tempNode.next
            if tempNode.random:
                clone.random = tempNode.random.next
            tempNode = clone.next
            
        tempNode = head
        newHead = head.next
        
        # Third pass
        while tempNode:
            clone = tempNode.next
            tempNode.next = clone.next
            if tempNode.next:
                clone.next = tempNode.next.next
            tempNode = tempNode.next
            
        return newHead
