#Doubly Linked List Forward-Backward Two-Pointer
#returns boolean

class Node:
    def init(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
def push(head, new_data):
  
    new_node = Node()
 
    if head != None:
        head.prev = new_node
        head = new_node
         
    return head
    
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

if __name__ == "__main__":
  
    head = None
    head = push(head, 'l')
    head = push(head, 'e')
    head = push(head, 'v')
    head = push(head, 'e')
    head = push(head, 'l')
 
    if isPalindrome(head):
        print("It is Palindrome")
    else:
        print("Not Palindrome")

#Output: It is a Palindrome
