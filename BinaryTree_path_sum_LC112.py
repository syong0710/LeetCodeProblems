class TreeNode:
    def __init__(self, nodeValue:int):
        self.value = nodeValue
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, rootValue):
        self.root = TreeNode(rootValue)

    # pre-order traversal of the binary tree
    def preOrderTrav(self, root:TreeNode)->list:
        if root is None:
            return []
        result = []
        self.__preOrder(root,result)
        return result

    def __preOrder(self, root:TreeNode, result:list):
        result.append(root.value)
        if root.left:
            self.__preOrder(root.left, result)
        if root.right:
            self.__preOrder(root.right, result)
        if root.left is None and root.left is None:
            return

    # path sum list
    def pathSum(self, root:TreeNode, sumTarget:int) -> bool:
        if root is None:
            return False
        sumList = []
        sum = 0
        self.__preOrderPaths(root, sum, sumList)
        print("The root-to-leaf path sum:" + str(sumList))
        for i in range(len(sumList)):
            if sumList[i] == sumTarget:
                return True
        return False


    def __preOrderPaths(self, root:TreeNode, sum:int, sumList:list):
        sum += root.value
        if root.left is None and root.right is None:
            sumList.append(sum)
            return
        if root.left:
            self.__preOrderPaths(root.left, sum, sumList)
        if root.right:
            self.__preOrderPaths(root.right, sum, sumList)



btree1 = BinaryTree(1)
btree1.root.left = TreeNode(2)
btree1.root.right = TreeNode(3)
btree1.root.left.left = TreeNode(4)
btree1.root.left.right = TreeNode(5)
btree1.root.right.right = TreeNode(7)


"""
           1
        /     \
       2       3
      /  \       \
     4   5        7
     
"""

print("Pre order traversal of the tree: " + str(btree1.preOrderTrav(btree1.root)))

sumTarget = 11
print("The sum target = "+ str(sumTarget))
print("if there is a root-to-leaf path sum equal to the target: "+ str(btree1.pathSum(btree1.root, sumTarget)))