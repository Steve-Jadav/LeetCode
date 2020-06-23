# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Problem 1305

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        inorder_1 = self.__inorder(root1)
        inorder_2 = self.__inorder(root2)
        result = list()
        
        i, j = 0, 0
        
        while i < len(inorder_1) and j < len(inorder_2):
            if inorder_1[i] <= inorder_2[j]:
                result.append(inorder_1[i])
                i += 1
            else:
                result.append(inorder_2[j])
                j += 1
        
        while i < len(inorder_1):
            result.append(inorder_1[i])
            i += 1

        while j < len(inorder_2):
            result.append(inorder_2[j])
            j += 1
            
        return result
    
    def __inorder(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        traversal = list()
        stack = list()
        current = root
        
        while True:
            
            if current:
                stack.append(current)
                current = current.left
                
            elif stack:
                current = stack.pop()
                traversal.append(current.val)
                current = current.right
            
            else:
                break
        
        return traversal
