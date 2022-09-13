class TreeNode:
    def __init__(self, nodeValue:int):
        self.value = nodeValue
        self.left = None
        self.right = None

class BST:
    def __init__(self, rootValue:int):
        self.root = TreeNode(rootValue)

    # in order traversal of the binayr tree
    def inOrderTrav(self, root:TreeNode) -> list:
        if root is None:
            return []
        nodeList = []
        self.inOrderRecur(root, nodeList)
        return nodeList

    def inOrderRecur(self, root:TreeNode, result:list):
        if root is None:
            return
        self.inOrderRecur(root.left, result)
        result.append(root.value)
        self.inOrderRecur(root.right, result)

    # level-order traversal of the tree:
    def levelOrderTrav(self, root:TreeNode) -> list:
        if root is None:
            return []
        nodeQue = []
        nodeQue.append(root)
        result = []
        while nodeQue:
            for _ in range(len(nodeQue)):
                nodeTemp = nodeQue.pop(0)
                result.append(nodeTemp.value)
                if nodeTemp.left:
                    nodeQue.append(nodeTemp.left)
                if nodeTemp.right:
                    nodeQue.append(nodeTemp.right)
        return result


    def insertNode(self, root:TreeNode, nodeKey:int) -> TreeNode:
        if root is None:
            return TreeNode(nodeKey)
        else:
            if nodeKey < root.value:
                root.left = self.insertNode(root.left, nodeKey)
                return root
            elif nodeKey > root.value:
                root.right = self.insertNode(root.right, nodeKey)
                return root
            elif nodeKey == root.value:
                return root

    def searchNode(self, root:TreeNode, target:int) -> TreeNode:
        if root is None:
            return root
        else:
            if target == root.value:
                return root
            elif target < root.value:
                return self.searchNode(root.left, target)
            elif target > root.value:
                return self.searchNode(root.right, target)


    def searchCloestValue(self, root:TreeNode, target:int):
        if root is None:
            return
        return self.preOrderCloest(root, target, float('inf'))

    def preOrderCloest(self, root: TreeNode, target:int, candidate:float):
        if root is None:
            return candidate
        else:
            if abs(target-root.value) < abs(target-candidate):
                candidate = root.value
            if target > root.value:
                return self.preOrderCloest(root.right, target, candidate)
            elif target < root.value:
                return self.preOrderCloest(root.left, target, candidate)
        return candidate

    def deleteNode(self, root:TreeNode, nodeValue:int) -> TreeNode:
        if root is None:
            return root
        # search the node with the nodeValue
        if nodeValue > root.value:
            root.right = self.deleteNode(root.right, nodeValue)
            return root
        elif nodeValue < root.value:
            root.left = self.deleteNode(root.left, nodeValue)
            return root
        else:
            if root.left is None and root.right is None:
                return None
            if root.left is None and root.right:
                return root.right
            if root.right is None and root.left:
                return root.left
            if root.left and root.right:
                node = root.right
                while node.left:
                    node = node.left
                node.left = root.left
                root = root.right
                return root



bst1 = BST(50)
bst1.insertNode(bst1.root, 25)
bst1.insertNode(bst1.root, 75)
bst1.insertNode(bst1.root, 60)
bst1.insertNode(bst1.root, 10)
bst1.insertNode(bst1.root, 20)
bst1.insertNode(bst1.root, 5)

"""
             50
         /        \
       25         75
     /          /
    10        60
  /   \
 5     20
      
"""


print("in-order traversal of the BST: " + str(bst1.inOrderTrav(bst1.root)))
print("level-order traversal of the BST: " + str(bst1.levelOrderTrav(bst1.root)))

search_target = 11
search_tree = bst1.searchNode(bst1.root, search_target)
print("level-order traversal of the searched tree: " + str(bst1.levelOrderTrav(search_tree)))

searchCloseTarget = 11
searchCloseValue = bst1.searchCloestValue(bst1.root, searchCloseTarget)
print("level-order traversal of the closest search tree: " + str(searchCloseValue))


deleteTarget = 10
deleteTree = bst1.deleteNode(bst1.root, deleteTarget)
print("level-order traversal of the deleted tree: " + str(bst1.levelOrderTrav(bst1.root)))