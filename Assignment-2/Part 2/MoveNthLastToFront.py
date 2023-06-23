#since we can only move one way in a linked list, both pointers will be
#at a fixed distance once they start moving
#Linked List Fixed Distance Two-Pointer

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=", ")
            temp = temp.next
        print()

    def moveNthLastToFront(self, n):
        temp = self.head
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
        if n > length:
            return
        temp = self.head
        for i in range(1, length - n + 1):
            temp = temp.next
        newHead = temp
        temp = temp.next
        newHead.next = None
        while temp is not None:
            temp = temp.next
        temp.next = self.head
        self.head = newHead

if __name__ == '__main__':
    llist = LinkedList()
    # swap the 2 nodes
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print("Linked List before moving last to front ")
    llist.printList()
      
    # Function call
    llist.move_nth_to_front(2)
    print("Linked List after moving last to front ")
    llist.printList()

#output: NoneType object has no attribute next
