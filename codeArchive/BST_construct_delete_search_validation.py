class TreeNode:
    def __init__(self, nodeValue):
        self.value = nodeValue
        self.left = None
        self.right = None

class BST:
    def __init__(self, rootValue):
        self.root = TreeNode(rootValue)

    def insertBST(self, root: TreeNode, target:int) -> TreeNode:
        if root is None:
            return TreeNode(target)
        else:
            if target > root.value:
                root.right = self.insertBST(root.right, target)
                return root
            if target < root.value:
                root.left = self.insertBST(root.left, target)
                return root
            if target == root.value:
                return root


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

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None # 节点为空，返回
        # search key value first
        if root.value < key:
            root.right = self.deleteNode(root.right, key)
            return root
        elif root.value > key:
            root.left = self.deleteNode(root.left, key)
            return root
        else: # the key has been found
            if root.left is None and root.right is None: return None
            # 当前节点的左子树为空，返回当前的右子树
            if root.left is None: return root.right
            # 当前节点的右子树为空，返回当前的左子树
            if root.right is None: return root.left
            # 左右子树都不为空，找到右孩子的最左节点 记为p
            if root.right and root.left:
                node = root.right # The right Child
                while node.left:
                    node = node.left # The left-most child of the right child
                # 将当前节点的左子树挂在p的左孩子上
                node.left = root.left
                # 当前节点的右子树替换掉当前节点，完成当前节点的删除
                root = root.right
                return root
            
    # check if the BST is valid        
    def validateBST(self, root: TreeNode) -> bool:
        return self.checkIsValidBST(root, float("inf"), -float("inf"))
    
    def checkIsValidBST(self, root:TreeNode, largerParentValue:float, smallerParentValue:float) -> bool:
        if root is None:
            return True
        if root.value >= largerParentValue:
            return False
        if root.value < smallerParentValue:
            return False

        leftBool = self.checkIsValidBST(root.left, root.value, smallerParentValue)
        rightBool = self.checkIsValidBST(root.right, largerParentValue, root.value)

        if leftBool and rightBool:
            return True
        else:
            return False




    # if the key contains in the tree
    def searchKey(self, root:TreeNode, target:int) -> TreeNode:
        if root is None:
            return root
        else:
            if target > root.value:
                return self.searchKey(root.right, target)
            elif target < root.value:
                return  self.searchKey(root.left, target)
            elif target == root.value:
                return root


    def ifContainKey(self, root:TreeNode, target:int)->bool:
        if self.searchKey(root, target) is None:
            return False
        else:
            return True



bst1 = BST(50)
#bst1.root.left = TreeNode(91)
#bst1.root.right = TreeNode(11)
bst1.insertBST(bst1.root, 25)
bst1.insertBST(bst1.root, 72)
bst1.insertBST(bst1.root, 21)
bst1.insertBST(bst1.root, 30)
bst1.insertBST(bst1.root, 88)
bst1.insertBST(bst1.root, 65)
bst1.insertBST(bst1.root, 18)
bst1.insertBST(bst1.root, 66)
bst1.insertBST(bst1.root, 64)
bst1.insertBST(bst1.root, 99)
bst1.insertBST(bst1.root, 80)

"""
             50
        /           \
      25             72
    /   \        /       \
   21    30     65        88
 /             /  \      /  \
18            64   66   80   99

"""
print("Level-order traversal of the tree: " + str(bst1.lvOrderTrav(bst1.root)))
print("if the tree a valid BST: " + str(bst1.validateBST(bst1.root)))

key_delete = 72
bst1.deleteNode(bst1.root, key_delete)
print("delete the node with value = " + str(key_delete))
print("Level-order traversal of the tree: " + str(bst1.lvOrderTrav(bst1.root)))

search_key = 64
nodeKey = bst1.searchKey(bst1.root, search_key)
print("Level-order traversal of the tree after searching: " + str(bst1.lvOrderTrav(nodeKey)))
print("If the key is in the tree: " + str(bst1.ifContainKey(nodeKey, search_key)))





