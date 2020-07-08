# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem 105
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        self.inorder_hashmap = dict()
        
        for i in range(0, len(inorder)):
            self.inorder_hashmap[inorder[i]] = i
            
        return self.buildTreeHelper(preorder, inorder, 0, len(inorder) - 1)
        
        
    def buildTreeHelper(self, preorder: List[int], inorder: List[int], start, end) -> TreeNode:
        
        if start > end:
            return None
        
        root = TreeNode(preorder.pop(0))
        
        if start == end:
            return root
        
        inorder_index = self.inorder_hashmap.get(root.val)
        root.left = self.buildTreeHelper(preorder, inorder, start, inorder_index - 1)
        root.right = self.buildTreeHelper(preorder, inorder, inorder_index + 1, end)
        
        return root
