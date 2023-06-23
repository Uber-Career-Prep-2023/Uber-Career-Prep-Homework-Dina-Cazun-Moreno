#need to use preorder traversal bc we need root in order to proceed cloning the rest of the BST
#use hash table
#recursively process the children

#returns root of new tree

class BinarySearchTree:
    def _init_(self, left, right, data):
        self.data = data
        self.left = None
        self.right = None

def copyTree(root):
    if not root:
        return None
        
    copy = BinarySearchTree(root.data)
    copy.left = copyTree(root.left)
    copy.right = copyTree(root.right)

    return copy

if __name__ == '__main__':
 
    root = BinarySearchTree(1)
    root.left = BinarySearchTree(2)
    root.right = BinarySearchTree(3)
    root.left.left = BinarySearchTree(4)
    root.left.right = BinarySearchTree(5)
    root.right.left = BinarySearchTree(6)
    root.right.right = BinarySearchTree(7)
 
    clone = copyTree(root)
 
    print('This is new tree: ')
    print(clone.val)
    
#output: prints 1, which is root of new copy of tree
