"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        
        traversal = list()
        stack = list()
        stack.append(root)
        
        while stack:
            x = stack.pop()
            traversal.insert(0, x.val)
            for child in x.children:
                stack.append(child)
        
        return traversal
