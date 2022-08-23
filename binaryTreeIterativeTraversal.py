class TreeNode:
    def __init__(self, nodeValue):
        self.value = nodeValue
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, nodeValue):
        self.root = TreeNode(nodeValue)

    # Recursive pre-order traversal of a binary tree, without using record as an input
    def recursivePreOrderTrav(self, root:TreeNode)->list:
        # create a local function to define the recursive process
        def traversal(root:TreeNode):
            if root is not None:
                result.append(root.value)
                traversal(root.left)
                traversal(root.right)
        # create a local void list as the input of the traversal
        result = []
        traversal(root)
        return result

    # Recursive in-order traversal of a binary tree, without using record as an input
    def recursiveInOrderTrav(self, root:TreeNode)->list:
        # create a local function to define the recursive process
        def traversal(root:TreeNode):
            if root is not None:
                traversal(root.left)
                result.append(root.value)
                traversal(root.right)
        # create a local void list as the input of the traversal
        result = []
        traversal(root)
        return result

    # Iterative pre-order traversal of a binary tree
    def interativePreOrderTrav(self, root:TreeNode)->list:
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            nodeTemp = stack.pop(0)
            result.append()



btree1 = BinaryTree(1)
btree1.root.left = TreeNode(2)
btree1.root.right = TreeNode(3)
btree1.root.left.left = TreeNode(4)
btree1.root.left.right = TreeNode(5)

#             1
#           /   \
#         2       3
#       /  \
#      4    5
#

print("In-order traversal (recursive) of the tree: " + str(btree1.recursiveInOrderTrav(btree1.root)))
print("Pre-order traversal (recursive) of the tree: " + str(btree1.recursivePreOrderTrav(btree1.root)))