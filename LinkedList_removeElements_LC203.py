# definition of a single-linked list
class LinkedListNode:
    def __init__(self, nodeValue:int):
        self.value = nodeValue
        self.next = None

class LinkedList:
    def __init__(self, headValue:int):
        self.head = LinkedListNode(headValue)

    def removeElements(self, head: LinkedListNode, target: int):
        while head and head.value==target:
            head = head.next
        nodeCur = head
        while nodeCur:
            while nodeCur.next and nodeCur.next.value==target:
                nodeCur.next = nodeCur.next.next
            nodeCur = nodeCur.next
        return head


    def linkedListTrav(self, head:LinkedListNode) -> list:
        if head is None:
            return []
        nodeCur = head
        result = []
        while nodeCur:
            result.append(nodeCur.value)
            nodeCur = nodeCur.next
        return result


linkedlist1 = LinkedList(1)
linkedlist1.head.next = LinkedListNode(3)
linkedlist1.head.next.next = LinkedListNode(4)
linkedlist1.head.next.next.next = LinkedListNode(6)
linkedlist1.head.next.next.next.next = LinkedListNode(7)
linkedlist1.head.next.next.next.next.next = LinkedListNode(9)
linkedlist1.head.next.next.next.next.next.next = LinkedListNode(9)
linkedlist1.head.next.next.next.next.next.next.next = LinkedListNode(11)
linkedlist1.head.next.next.next.next.next.next.next.next = LinkedListNode(12)

print("The elements of the linked list: " + str(linkedlist1.linkedListTrav(linkedlist1.head)))

linkedlist1_rm1 = linkedlist1.removeElements(linkedlist1.head, 12)
print("The elements of the linked list: " + str(linkedlist1.linkedListTrav(linkedlist1_rm1)))








