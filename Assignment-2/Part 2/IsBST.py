#inorder traversal because we want to sort
#for a tree to be BST, left has to be less than root and right has to be greater than root

#inorder: left, root, right
#return boolean

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def isBST(node, minVal = float('-inf'), maxVal = float('inf')):
    if node is None:
        return True
    if node.data < minVal or node.data > maxVal:
        return False
    return isBST(node.left, minVal, node.data - 1) and isBST(node.right, node.data + 1, maxVal)

if __name__ == "__main__":
  root = Node(4)
  root.left = Node(2)
  root.right = Node(5)
  # root.right.left = Node(7)
  root.left.left = Node(1)
  root.left.right = Node(3)
 
  # Function call
  if is_bst(root) is True:
      print("Is BST")
  else:
      print("Not a BST")

#output: Is BST
