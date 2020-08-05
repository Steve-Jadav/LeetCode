# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root == None:
            return root
        
        pointer: TreeNode = root
        stack = list()
        counter = 0
        
        while True:
            if pointer:
                stack.append(pointer)
                pointer = pointer.left
            
            elif stack:
                pointer = stack.pop()
                counter += 1 
                if counter == k:
                    return pointer.val
                pointer = pointer.right
            
            else:
                break
                
        return None
