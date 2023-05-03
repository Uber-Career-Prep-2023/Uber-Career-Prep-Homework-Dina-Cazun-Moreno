#def use hashtable to find frequency of nodes
#Hash Linked List Nodes technique

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

    def dedupSortedList(head):
        curr = head
        prev = None
        duplicateCounter = dict()
        while curr:
            if curr.data not in duplicateCounter:
                duplicateCounter[curr.data] = None
                prev = curr
            else:
                prev.next = curr.next

            curr = curr.next
