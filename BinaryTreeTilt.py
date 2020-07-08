# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root == None:
            return 0

        tilt = [0]
        self.helper(root, tilt)
        return tilt[0]

    def helper(self, root: TreeNode, tilt: List) -> int:
        if root == None:
            return 0

        left = self.helper(root.left, tilt)
        right = self.helper(root.right, tilt)

        tilt[0] += abs(left - right)

        return left + right + root.val
