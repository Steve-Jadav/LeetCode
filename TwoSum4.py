# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        if root is None:
            return False
        
        hashset = set()
        queue = list()
        queue.append(root)
        
        while queue:
            node = queue.pop(0)
            complement = k - node.val
            
            if complement in hashset:
                return True
            else:
                hashset.add(node.val)
            
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            
        
        return False
