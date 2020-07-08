# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True

        return self.helper(root.left, root.right)

    def helper(self, root1, root2):

        if root1 == None and root2 == None:
            return True

        if root1 and root2:
            if root1.val == root2.val:
                return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)

        return False



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True

        stack = list()
        stack.append([root.left, root.right])

        while stack:
            left, right = stack.pop()

            if left == None and right == None:
                continue

            if left == None or right == None:
                return False

            if left.val == right.val:
                stack.append([left.left, right.right])
                stack.append([left.right, right.left])

            else:
                return False

        return True
