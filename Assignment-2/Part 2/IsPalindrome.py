#Doubly Linked List Forward-Backward Two-Pointer
#returns boolean

class Node:
    def init(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
    def isPalindrome(head) -> bool:
        if head == None:
            return True
    
        end = head
        while end.next != None:
            end = end.next

        while head != end:
            if head.data != end.data:
                return False
            
            head = head.next
            end = end.prev

        return True
