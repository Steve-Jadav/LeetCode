# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None

        inorder_traversal = self.__inorder(root)
        root_node = TreeNode(0)

        for node_val in inorder_traversal:
            temp_node = TreeNode(node_val)
            root_node.right = temp_node
            temp_node = temp_node.right

        return root_node.right


    def __inorder(self, root: TreeNode) -> List:
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


# APPROACH 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.current.right = node
                self.current = node
                inorder(node.right)

        rootNode = TreeNode(0)
        self.current = rootNode
        inorder(root)
        return rootNode.right
