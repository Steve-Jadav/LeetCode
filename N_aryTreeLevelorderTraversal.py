"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        
        queue = [root]
        traversal = list()
        
        while queue:
            next_level = list()
            size = len(queue)
            for i in range(0, size):
                x = queue.pop(0)
                next_level.append(x.val)
                for child in x.children:
                    queue.append(child)
            
            traversal.append(next_level)
        
        return traversal
