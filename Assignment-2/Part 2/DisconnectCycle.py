#Linked List Fast-Slow Two Pointer
#Hash Linked List Nodes

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

    def disconnectCycle(head):
        curr = head
        prev = None

        nodes = set()

        while curr:
            if curr in nodes:
                prev.next = None
                return
            nodes.add(curr)
            prev = curr
            curr = curr.next
