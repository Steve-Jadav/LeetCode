# Problem 707.
# Approach: Design a Doubly Linked List with a tail pointer.

class Node:
    
    def __init__(self, val: int = None):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

        
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        
        elif index == 0:
            return self.head.val
        
        elif index == self.size - 1:
            return self.tail.val
        
        temp: Node = self.head
            
        for _ in range(0, index):
            temp = temp.next
        
        return temp.val
        
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
        
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        
        self.size += 1

        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
        
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        
        self.size += 1
    

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size or index < 0:
            return None
        elif index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            newNode = Node(val)
        
            # Traverse from the head
            if index <= abs(self.size - index):
                temp = self.head
                for _ in range(0, index - 1):
                    temp = temp.next
                
            # Traverse from the tail
            else:
                temp = self.tail
                for _ in range(self.size - 1, index - 1, -1):
                    temp = temp.prev
            
            newNode.next = temp.next
            newNode.prev = temp    
            temp.next.prev = newNode
            temp.next = newNode
        
            self.size += 1

            
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size or index < 0:
            return None
        
        # Only one element in the list
        elif index == 0 and self.size == 1:
            self.head = None
            self.tail = None
        
        # More than one element in the list
        elif index == 0:
            self.head = self.head.next
            
        elif index == self.size - 1:
            self.tail = self.tail.prev
        
        else:
            temp = self.head
            for _ in range(0, index):
                temp = temp.next
            # temp points to the node that is supposed to be deleted
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            del temp

        self.size -= 1
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
