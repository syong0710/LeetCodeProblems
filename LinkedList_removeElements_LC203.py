class LinkedListNode:
    def __init__(self, nodeValue:int):
        self.value = nodeValue
        self.next = None

class LinkedList:
    def __init__(self, headValue):
        self.head = LinkedListNode(headValue)

    def addNode(self, head: LinkedListNode, nodeValue:int):
        if head is None:
            head = LinkedListNode(nodeValue)
        else:
            nodeTmp = head
            while nodeTmp.next:
                nodeTmp = nodeTmp.next
            nodeTmp.next = LinkedListNode(nodeValue)



    def linkedListTrav(self, head:LinkedListNode) -> list:
        if head is None:
            return []
        result = []
        nodeTmp = head
        result.append(nodeTmp.value)
        while nodeTmp.next:
            nodeTmp = nodeTmp.next
            result.append(nodeTmp.value)
        return result

    # delete elements without creating a dummy head
    def deleteElements1(self, head:LinkedListNode, target:int) -> LinkedListNode:
        if head is None:
            return head

        # Create a dummy head
        head_dummy = LinkedListNode(-1)
        head_dummy.next = head

        # iteration from head to tail
        nodeCur = head_dummy
        while nodeCur.next:
            if nodeCur.next.value == target:
                nodeCur.next = nodeCur.next.next
            else:
                nodeCur = nodeCur.next

        return head_dummy.next


linkedList1 = LinkedList(1)
linkedList1.addNode(linkedList1.head,1)
linkedList1.addNode(linkedList1.head,1)
linkedList1.addNode(linkedList1.head,3)
linkedList1.addNode(linkedList1.head,7)
linkedList1.addNode(linkedList1.head,9)
linkedList1.addNode(linkedList1.head,11)
linkedList1.addNode(linkedList1.head,11)
linkedList1.addNode(linkedList1.head,13)
linkedList1.addNode(linkedList1.head,11)
linkedList1.addNode(linkedList1.head,17)
linkedList1.addNode(linkedList1.head,17)

print("The linked list:" + str(linkedList1.linkedListTrav(linkedList1.head)))

linkedList1_rmHead = linkedList1.deleteElements1(linkedList1.head, 11)
print("The linked list with the target elements removed:" + str(linkedList1.linkedListTrav(linkedList1_rmHead)))



