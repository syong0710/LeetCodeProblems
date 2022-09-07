class TreeNode:
    def __init__(self, nodeValue:int):
        self.value = nodeValue
        self.left = None
        self.right = None

class BST:
    def __init__(self, rootValue:int):
        self.root = TreeNode(rootValue)

    # Insert nodes into the binary search tree
    def insertNode(self, root:TreeNode, nodeValue:int)->TreeNode:
        if root is None:
            return TreeNode(nodeValue)
        else:
            if nodeValue < root.value:
                root.left = self.insertNode(root.left, nodeValue)
                return root
            elif nodeValue > root.value:
                root.right = self.insertNode(root.right, nodeValue)
                return root
            elif nodeValue == root.value:
                return root


    # in-order traversal of the binary tree
    def inOrderTrav(self, root:TreeNode) -> list:
        if root is None:
            return []
        result = []
        self._inOrder(root, result)
        return result

    def _inOrder(self, root:TreeNode, result: list):
        if root is None:
            return
        else:
            self._inOrder(root.left, result)
            result.append(root.value)
            self._inOrder(root.right, result)

    # check if the BST is valid: the output of the in-order traversal should be sorted
    def isValidBST(self, root:TreeNode)->bool:
        inOrderList = self.inOrderTrav(root)
        return self._isSorted(inOrderList)


    def _isSorted(self, inputArray:list)->bool:
        for i in range(1, len(inputArray)):
            # notice that BST cannot have duplicated element
            if inputArray[i] <= inputArray[i-1]:
                return False
        return True



btree1 = BST(50)
btree1.insertNode(btree1.root, 25)
btree1.insertNode(btree1.root, 75)
btree1.insertNode(btree1.root, 30)
btree1.insertNode(btree1.root, 20)
btree1.insertNode(btree1.root, 70)

"""
            50
         /      \
        25        75
       /  \       /      
     20    30    70   

"""

print("In-order traversal of the tree: " + str(btree1.inOrderTrav(btree1.root)))
print("if the BST is valid:  " + str(btree1.isValidBST(btree1.root)))



btree1.root.right.right = TreeNode(1)
"""
            50
         /      \
        25        75
       /  \       /  \    
     20    30    70   1

"""
print("In-order traversal of the tree: " + str(btree1.inOrderTrav(btree1.root)))
print("if the BST is valid:  " + str(btree1.isValidBST(btree1.root)))