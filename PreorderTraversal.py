# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        traversal = list()
        stack = list()
        stack.append(root)
        
        while stack:
            current = stack.pop()
            traversal.append(current.val)
            
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        
        return traversal
