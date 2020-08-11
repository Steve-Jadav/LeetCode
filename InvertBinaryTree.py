# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    
    def __swap(self, node: TreeNode) -> None:
        if node == None:
            return
        
        temp = node.left
        node.left = node.right
        node.right = temp
        
        
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        
        queue = deque()
        queue.append(root)
        
        while queue:
            current = queue.popleft()
            self.__swap(current)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
                
        return root
