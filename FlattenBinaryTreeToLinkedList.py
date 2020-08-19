# Problem 114

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root
        
        stack = list()
        temp = root
        
        while root or stack:
            if root.right:
                stack.append(root.right)
            
            root.right = root.left
            root.left = None
            
            if root.right == None and stack:
                root.right = stack[-1]
                stack.pop()
                
            root = root.right
        
        return temp
