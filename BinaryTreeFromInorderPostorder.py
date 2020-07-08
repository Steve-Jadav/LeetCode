# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem 106
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.inorder_hashmap = dict()
        
        for i in range(0, len(inorder)):
            self.inorder_hashmap[inorder[i]] = i
        
        return self.buildTreeHelper(inorder, postorder, 0, len(inorder) - 1)
    
    def buildTreeHelper(self, inorder: List[int], postorder: List[int], start: int, end: int) -> TreeNode:
        
        if start > end:
            return None
        
        root = TreeNode(postorder.pop())
        
        if start == end:
            return root
        
        inorder_index = self.inorder_hashmap.get(root.val)
        root.right = self.buildTreeHelper(inorder, postorder, inorder_index + 1, end)
        root.left = self.buildTreeHelper(inorder, postorder, start, inorder_index - 1)
        return root
