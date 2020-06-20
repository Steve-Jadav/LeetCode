# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.index = -1
        self.sorted_nodes = list()
        self.__inorder(root)

    def __inorder(self, root: TreeNode):
        stack = list()
        current = root

        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                self.sorted_nodes.append(current.val)
                current = current.right
            else:
                break

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.sorted_nodes[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index < len(self.sorted_nodes) - 1

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
