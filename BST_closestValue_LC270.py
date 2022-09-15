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


    def closestNodeVal(self, root:TreeNode, target:int) -> float:
        return self.searchClosestVal(root, target, float("inf"))

    def searchClosestVal(self, root:TreeNode, target:int, candidate:float)->float:
        if root is None:
            return candidate
        if abs(target - root.value) < abs(target - candidate):
            candidate = root.value

        if target < root.value:
            candidate = self.searchClosestVal(root.left, target, candidate)
        if target > root.value:
            candidate = self.searchClosestVal(root.right, target, candidate)

        return candidate




bst1 = BST(50)
bst1.insertNode(bst1.root, 75)
bst1.insertNode(bst1.root, 25)
bst1.insertNode(bst1.root, 85)
bst1.insertNode(bst1.root, 15)
bst1.insertNode(bst1.root, 30)
bst1.insertNode(bst1.root, 35)
bst1.insertNode(bst1.root, 22)
bst1.insertNode(bst1.root, 11)


"""
               50
           /       \
         25         75
        /   \         \
      15     30        85    
     /   \     \
    11   22     35
"""


print("level order traversal of the BST: " + str(bst1.levOrderTrav(bst1.root)))

searchVal = 24
print("The closest value to the " + str(searchVal) + " is " + str(bst1.closestNodeVal(bst1.root, searchVal)))