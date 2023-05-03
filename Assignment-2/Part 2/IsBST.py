#inorder traversal because we want to sort
#for a tree to be BST, left has to be less than root and right has to be greater than root

#inorder: left, root, right
#return boolean

def isBST(root) -> bool:
    nodes = []
    
    def inorderTraversal(root):
        if root is None:
            return None
        inorderTraversal(root.left)
        nodes.append(root)
        inorderTraversal(root.right)
    
    inorderTraversal(root)
    if nodes == list(sorted(set(nodes))):
        return True
    else:
        return False
