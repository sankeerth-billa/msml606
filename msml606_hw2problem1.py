class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class HomeWork2:
    def constructBinaryTree(self, input) -> TreeNode:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in input:
            if token in operators:
                right = stack.pop()
                left = stack.pop()
                node = TreeNode(token)
                node.left = left
                node.right = right
                stack.append(node)
            else:
                stack.append(TreeNode(token))
        return stack.pop()