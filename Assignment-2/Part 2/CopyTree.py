#need to use preorder traversal bc we need root in order to proceed cloning the rest of the BST
#use hash table
#recursively process the children

#returns root of new tree

class BinarySearchTree:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

    def copyTree(root):
        if root is None:
            return None
        
        copy = BinarySearchTree(root.data)
        copy.left = copyTree(root.left)
        copy.right = copyTree(root.right)

        return copy
