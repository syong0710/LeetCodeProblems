class TreeNode:
    def __init__(self, nodeValue:int):
        self.value = nodeValue
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, rootValue:int):
        self.root = TreeNode(rootValue)

    # insert the node using recursion
    def insertNode(self, root:TreeNode, nodeValue:int):
        if root is None:
            return TreeNode(nodeValue)
        else:
            if root.value == nodeValue:
                return root
            elif root.value < nodeValue:
                root.right = self.insertNode(root.right, nodeValue)
            else:
                root.left = self.insertNode(root.left, nodeValue)
        return root

    # search BST using recursive method
    def searchBST_recursive(self, root:TreeNode, searchVal:int) -> TreeNode:
        if root is None:
            return root
        if root.value == searchVal:
            return root
        if root.value > searchVal:
            return self.searchBST_recursive(root.left, searchVal)
        if root.value < searchVal:
            return self.searchBST_recursive(root.right, searchVal)

    # search BST using iterative method
    def searchBST_inter(self, root:TreeNode, searchVal:int)->TreeNode:
        if root is None:
            return root
        while root:
            if searchVal == root.value:
                return root
            if searchVal<root.value:
                root = root.left
            if searchVal>root.value:
                root = root.right
        return None


    # in-order recursive print
    def inOrder_list(self, root:TreeNode):
        if root is None:
            return []
        results = []
        self.inOrderTrav(root, results)
        return results

    def inOrderTrav(self, root:TreeNode, results):
        if root is None:
            return
        self.inOrderTrav(root.left, results)
        results.append(root.value)
        self.inOrderTrav(root.right, results)


tree1 = BinarySearchTree(10)
tree1.insertNode(tree1.root,7)
tree1.insertNode(tree1.root,20)
tree1.insertNode(tree1.root,25)
tree1.insertNode(tree1.root,8)
tree1.insertNode(tree1.root,14)
tree1.insertNode(tree1.root,5)

"""

           10
        /      \
      7         20
    /  \        /  \
   5    8    14     25

"""
print("in-order traversal of the BST: " + str(tree1.inOrder_list(tree1.root)))

tree1Search = tree1.searchBST_recursive(tree1.root, 20)
print("BST search results" + str(tree1.inOrder_list(tree1Search)))

tree2Search = tree1.searchBST_inter(tree1.root, 7)
print("BST search results" + str(tree1.inOrder_list(tree2Search)))


