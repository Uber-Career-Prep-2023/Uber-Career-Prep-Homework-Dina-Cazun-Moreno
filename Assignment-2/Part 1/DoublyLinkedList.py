#Question 2: Doubly Linked List
class Node:
    def init(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def insertAtFront(head, val):
        newNode = Node(head, val)
        newNode.prev = None
        newNode.next = head

        if head is not None:
            head.prev = newNode

        head = newNode
        return head

    def insertAtBack(head, val):
        newNode = Node(head, val)
        lastNode = head
        newNode.next = None

        if head is None:
            newNode.prev = None
            head = newNode

        while lastNode.next is not None:
            lastNode = lastNode.next

        lastNode.next = newNode
        newNode.prev = lastNode

    def insertAfter(head, val, loc):
        if loc is None:
            print("Node DNE")
        
        newNode = Node(head, val)
        newNode.next = loc.next
        loc.next = newNode
        newNode.prev = loc

        if newNode.next is not None:
            newNode.next.prev = newNode

    def deleteFront(head):
        if head != None:
            temp = head
            head = head.next
            temp = None
        
        if head != None:
            head.prev = None
        
        return head
    
    def deleteBack(head):
        if head != None:
            if head.next == None:
                head = None
            else:
                temp = head
                while temp.next.next != None:
                    temp = temp.next
                last = temp.next
                temp.next = None
                last = None

    def deleteNode(head, loc):
        if head is None or loc is None:
            return
        if head == loc:
            head = head.next
        if loc.next is not None:
            loc.next.prev = loc.prev
        if loc.prev is not None:
            loc.prev.next = loc.next
