# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.inorder = list()
        stack = list()
        current = root
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                self.inorder.append(current.val)
                current = current.right
            else:
                break

    def next(self) -> int:
        """
        @return the next smallest number
        """
        x = self.inorder.pop(0)
        return x
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.inorder:
            return True
        
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
