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

    # Check if the targetSum is included in the root-to-leaf path sum
    def checkPathSum(self, root:TreeNode, targetSum:int) -> bool:
        if root is None:
            return False
        sumList = self.getPathSum(root)
        for i in range(len(sumList)):
            if sumList[i] == targetSum:
                return True
        return False

    # get the root-to-leaf path sum list
    def getPathSum(self, root:TreeNode) -> list:
        if root is None:
            return []
        sumList = []
        sumCur = 0
        self.pathSumRecur(root, sumCur, sumList)
        return sumList

    def pathSumRecur(self, root:TreeNode, sumCur:int, sumList:list):
        if root is None:
            sumList = []

        sumCur += root.value
        if root.left is None and root.right is None:
            sumList.append(sumCur)
            # Backtrack:
            sumCur -= root.value
            return

        if root.left:
            self.pathSumRecur(root.left, sumCur, sumList)
        if root.right:
            self.pathSumRecur(root.right, sumCur, sumList)
        # Backtrack:
        sumCur -= root.value


btree1 = BinaryTree(5)
btree1.root.left = TreeNode(4)
btree1.root.right = TreeNode(8)
btree1.root.left.left = TreeNode(11)
btree1.root.right.left = TreeNode(13)
btree1.root.right.right = TreeNode(4)
btree1.root.left.left.left = TreeNode(7)
btree1.root.left.left.right = TreeNode(2)
btree1.root.right.right.left = TreeNode(5)
btree1.root.right.right.right = TreeNode(1)
btree1.root.right.right.right = TreeNode(1)
btree1.root.right.right.right = TreeNode(1)
btree1.root.right.right.right.right = TreeNode(9)


"""
               5
          /           \
        4              8
       /              /   \
     11              13    4     
    /   \                 /  \  
   7     2               5     1
                                \
                                 9
"""

print("Pre-order traversal of the binary tree: " + str(btree1.preOrderTrav(btree1.root)))

print("All paths of the binary tree: " + str(btree1.getPathSum(btree1.root)))

target_sum = 22
print("The target sum is: " + str(target_sum))
print("If the target is included in the root-to-leaf path sum: " + str(btree1.checkPathSum(btree1.root, target_sum)))
