#PART 1
#Question 1: Singly Linked List

class Node:
    def init(self, data):
        self.data = data
        self.next = None

    def insertAtFront(head, val):
        temp = Node(None, None)
        newHead = Node(head, val)
        newHead.next = temp
        temp = newHead
        return temp

    def insertAtBack(head, val):
        prevNode = Node(None, None)
        newNode = (head, val)
        prevNode.next = newNode

    def insertAfter(head, val, loc):
        newNode = Node(head, val)
        loc.next = newNode

    def deleteFront(head):
        if not head:
            return None
        
        temp = head
        head = head.next
        temp = None
        return head
    
    def deleteBack(head):
        if head.next == None:
            head = None

        secondToLast = head
        while(secondToLast.next.next):
            secondToLast = secondToLast.next
        secondToLast.next = None

    def deleteNode(head, loc):
        while head is not loc:
            head = head.next
        head.val = head.next.val
        head.next = head.next.next
        

    def length(head) -> int:
        #while there is a head.next, keep incrementing
        count = 1 #because we are given a node

        if head.next:
            count += 1

        return count

    def reverseIterative(head):
        #3 pointers: prev, cur, next
        prev = None
        cur = head

        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        head = prev


    def reverseRecursive(head):
        #base case
        if head is None or head.next is None:
            return head
        
        #recursive callrr
        listLeft = head.reverseRecursive(head.next)

        head.next.next = head
        head.next = None

        return listLeft
