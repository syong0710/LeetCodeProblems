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

    # Recursive post-order traversal of a binary tree, without using record as an input
    def recursivePostOrderTrav(self, root:TreeNode)->list:
        def traversal(root:TreeNode):
            if root:
                traversal(root.left)
                traversal(root.right)
                result.append(root.value)
        result = []
        traversal(root)
        return result

    # Iterative pre-order traversal of a binary tree (the non-uniform format)
    def interativePreOrderTrav(self, root:TreeNode)->list:
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            # the top of the stack
            nodeTemp = stack.pop(-1)
            result.append(nodeTemp.value)
            # the right child first, then the left child
            # so the left child is on the top, and will pop first
            if nodeTemp.right:
                stack.append(nodeTemp.right)
            if nodeTemp.left:
                stack.append(nodeTemp.left)
        return result

    # The uniform format of the iterative Preorder traversal
    def interativePreOrderTrav_uniform(self, root: TreeNode) -> list:
        result = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            # pop the root first
            nodeTmp = stack.pop()
            if nodeTmp is not None:
                # for pre-order:
                # stack the right child fist, then stack the left child, at last stack the root
                if nodeTmp.right:
                    stack.append(nodeTmp.right)
                if nodeTmp.left:
                    stack.append(nodeTmp.left)
                stack.append(nodeTmp)
                stack.append(None)
            else:
                # if the current node is none, pop the next one from the stack
                nodeTmp = stack.pop()
                result.append(nodeTmp.value)
        return result

    # The uniform format of the iterative Inorder traversal
    def interativeInOrderTrav_uniform(self, root: TreeNode) -> list:
        result = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            # pop the root first
            nodeTmp = stack.pop()
            if nodeTmp is not None:
                # for in-order:
                # stack the right child fist, then stack the root, at last the left child,
                if nodeTmp.right:
                    stack.append(nodeTmp.right)
                stack.append(nodeTmp)
                stack.append(None)
                if nodeTmp.left:
                    stack.append(nodeTmp.left)
            else:
                # if the current node is none, pop the next one from the stack
                nodeTmp = stack.pop()
                result.append(nodeTmp.value)
               #print(result)
        return result

#
#             1
#           /   \
#         2       3
#       /  \
#      4    5
#

btree1 = BinaryTree(1)
btree1.root.left = TreeNode(2)
btree1.root.right = TreeNode(3)
btree1.root.left.left = TreeNode(4)
btree1.root.left.right = TreeNode(5)



print("Pre-order traversal (recursive) of the tree: " + str(btree1.recursivePreOrderTrav(btree1.root)))
print("Pre-order traversal (iterative, non-uniform) of the tree: " + str(btree1.interativePreOrderTrav(btree1.root)))
print("Pre-order traversal (iterative, uniform) of the tree: " + str(btree1.interativePreOrderTrav_uniform(btree1.root)))

print("In-order traversal (recursive) of the tree: " + str(btree1.recursiveInOrderTrav(btree1.root)))
print("In-order traversal (iterative, uniform) of the tree: " + str(btree1.interativeInOrderTrav_uniform(btree1.root)))


print("Post-order traversal (recursive) of the tree: " + str(btree1.recursivePostOrderTrav(btree1.root)))
#print("Post-order traversal (iterative) of the tree: " + str(btree1.interativePostOrderTrav(btree1.root)))
