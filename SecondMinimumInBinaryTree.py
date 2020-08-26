# Problem 671

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        uniques = set()
        self.dfs(root, uniques)
        
        min1, ans = root.val, float('inf')
        for val in uniques:
            if min1 < val < ans:
                ans = val
        
        return ans if ans < float('inf') else -1
    
    def dfs(self, root, uniques):
        if root:
            uniques.add(root.val)
            self.dfs(root.left, uniques)
            self.dfs(root.right, uniques)
