class TreeNode:
    def __init__(self, nodeValue:int):
        self.value = nodeValue
        self.left = None
        self.right = None

class BST:
    def __init__(self, rootValue:int):
        self.root = TreeNode(rootValue)

    def insertNode(self, root:TreeNode, nodeValue:int) -> TreeNode:
        if root is None:
            return TreeNode(nodeValue)
        else:
            if nodeValue > root.value:
                root.right = self.insertNode(root.right, nodeValue)
                return root
            elif nodeValue < root.value:
                root.left = self.insertNode(root.left, nodeValue)
                return root
            elif nodeValue == root.value:
                return root

    def levOrderTrav(self, root:TreeNode) ->list:
        if root is None:
            return []
        result = []
        nodeStack = []
        nodeStack.append(root)
        while nodeStack:
            for _ in range(len(nodeStack)):
                nodeTemp = nodeStack.pop(0)
                result.append(nodeTemp.value)
                if nodeTemp.left:
                    nodeStack.append(nodeTemp.left)
                if nodeTemp.right:
                    nodeStack.append(nodeTemp.right)
        return result

    def deleteNode(self, root:TreeNode, nodeValue:int)->TreeNode:
        if root is None:
            return root
        if nodeValue > root.value:
            root.right = self.deleteNode(root.right, nodeValue)
            return root
        if nodeValue < root.value:
            root.left = self.deleteNode(root.left, nodeValue)
            return root
        else:
            if root.left is None and root.right is None:
                return None
            if root.left is None and root.right:
                return root.right
            if root.right is None and root.left:
                return root.left
            if root.right and root.left:
                node = root.right
                while node.left:
                    node = node.left
                node.left = root.left
                root = root.right
                return root




bst1 = BST(50)
bst1.insertNode(bst1.root, 75)
bst1.insertNode(bst1.root, 25)
bst1.insertNode(bst1.root, 85)
bst1.insertNode(bst1.root, 15)
bst1.insertNode(bst1.root, 30)
bst1.insertNode(bst1.root, 35)
bst1.insertNode(bst1.root, 22)
bst1.insertNode(bst1.root, 11)
bst1.insertNode(bst1.root, 28)

"""
               50
            /       \
           25         75
         /     \         \
       15       30         85    
     /   \     /  \
    11   22   28   35
"""


print("level order traversal of the BST: " + str(bst1.levOrderTrav(bst1.root)))

delNodeVal = 99
bst1_del = bst1.deleteNode(bst1.root, delNodeVal)
print("delete the node with value = " + str(delNodeVal))
print("level order traversal of the BST after deleting the node: " + str(bst1.levOrderTrav(bst1_del)))





