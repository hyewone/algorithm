# linkedList - 링크드리스트

class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount or self.nodeCount == 0:
            raise IndexError('out of array')

        if pos == 1:
            curr = self.head
            if self.nodeCount == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

        else:
            prev = self.getAt(pos - 1)
            if pos == self.nodeCount:
                curr = self.tail
                prev.next = None
                self.tail = prev
            else:
                curr = prev.next
                after = curr.next
                prev.next = after

        self.nodeCount -= 1
        return curr.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next

class Conversion:

    def linkedListToLists(list):
        temp = []
        for i in range(list.nodeCount):
            temp.append(list.getAt(i + 1).data)
        return temp


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
linkedList = LinkedList()
linkedList.insertAt(1,n1)
linkedList.insertAt(2,n2)
linkedList.insertAt(3,n3)
print(Conversion.linkedListToLists(linkedList))
linkedList.popAt(2)
print(Conversion.linkedListToLists(linkedList))
