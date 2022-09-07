class TreeNode:
    def __init__(self, nodeValue):
        self.value = nodeValue
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, rootValue):
        self.root = TreeNode(rootValue)

    # preOrder traversal of the binary tree
    def preOrderTrav(self, root:TreeNode)->list:
        if root is None:
            return []
        result = []
        self._preOrder(root,result)
        return result

    def _preOrder(self, root: TreeNode, result:list):
        if root is None:
            return
        else:
            result.append(root.value)
            self._preOrder(root.left, result)
            self._preOrder(root.right, result)

    # use the idea of preOrder traversal, get all the path of the tree
    def binaryTreePaths(self, root:TreeNode)->list:
        if root is None:
            return []
        result = []
        path = ''
        self._preOrderPath(root,path,result)
        return result


    def _preOrderPath(self, root:TreeNode, path:str, result:list):
        # Pre-order
        path += str(root.value)
        if root.left is None and root.right is None:
            result.append(path)
        if root.left:
            self._preOrderPath(root.left, path+ " -> ", result)
        if root.right:
            self._preOrderPath(root.right, path+ " -> ", result)




btree1 = BinaryTree(1)
btree1.root.left = TreeNode(2)
btree1.root.right = TreeNode(3)
btree1.root.left.left = TreeNode(4)
btree1.root.left.right = TreeNode(5)

"""
            1
        /      \
       2        3
     /  \
    4    5

"""

print("Pre-order traversal of the binary tree: " + str(btree1.preOrderTrav(btree1.root)))
print("All paths of the binary tree: " + str(btree1.binaryTreePaths(btree1.root)))