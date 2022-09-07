class TreeNode:
    def __init__(self, nodeValue:int):
        self.value = nodeValue
        self.left = None
        self.right = None

class BSTree:
    def __init__(self, rootValue:int):
        self.root = TreeNode(rootValue)

    def lvOrderTrav(self, root:TreeNode):
        if root is None:
            return []
        result = []
        nodeQue = []
        nodeQue.append(root)
        while nodeQue:
            for _ in range(0, len(nodeQue)):
                nodeTemp = nodeQue.pop(0)
                result.append(nodeTemp.value)
                if nodeTemp.left:
                    nodeQue.append(nodeTemp.left)
                if nodeTemp.right:
                    nodeQue.append(nodeTemp.right)
        return result

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

    def searchNode(self, root:TreeNode, searchNum:int)->TreeNode:
        if root is None:
            return root
        else:
            if root.value == searchNum:
                return root
            elif searchNum < root.value:
                return self.searchNode(root.left, searchNum)
            elif searchNum > root.value:
                return self.searchNode(root.right, searchNum)




bstree1 = BSTree(50)
bstree1.insertNode(bstree1.root, 25)
bstree1.insertNode(bstree1.root, 75)
bstree1.insertNode(bstree1.root, 80)
bstree1.insertNode(bstree1.root, 20)
bstree1.insertNode(bstree1.root, 30)

"""

                  50
                /     \
               25      75
              /  \        \
            20   30        80

"""

print("level-order traversal of the tree: " + str(bstree1.lvOrderTrav(bstree1.root)))

searchKey = 25
bstree1_search = bstree1.searchNode(bstree1.root, searchKey)
print("level-order traversal of the search result: " + str(bstree1.lvOrderTrav(bstree1_search)))



