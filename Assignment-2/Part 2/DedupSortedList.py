#def use hashtable to find frequency of nodes
#Hash Linked List Nodes technique

class Node:
    def _init_(self, data, next):
        self.data = data
        self.next = None

def dedupSortedList(head):
    curr = head
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

if __name__ == "__main__":
  root = Node(1, root.next)
  root.next = Node(2, root.next.next)
  root.next.next = Node(2)
  print(root)

#Trying to test but output says root is not defined?
