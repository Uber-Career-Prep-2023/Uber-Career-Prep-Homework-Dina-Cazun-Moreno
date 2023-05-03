class BinarySearchTree:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

    def min():
        while root.left is not None:
            root = root.left
        return root.data
    
    def max():
        while root.right:
            root = root.right
        return root.data
    
    def contains(val) -> bool:
        #returns boolean
        root = BinarySearchTree(root)
        if root is None or root.data == val:
            return root
        
        if root.data < val:
            return root.right.contains(val)
        
        return root.left.contains(val)
    
    def insert(val):
        root = BinarySearchTree(root)
        if root is None:
            print("None")
        else:
            if root.data == val:
                return root
            elif root.data < val:
                root.right = root.right.insert(val)
            else:
                root.left = root.left.insert(val)

    def delete(val) -> int:
        #returns int
        root = BinarySearchTree(root)
        if root is None:
            return root
        if val < root.data:
            root.left = root.left.delete(val)
        elif val > root.data:
            root.right = root.right.delete(val)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            temp = min(root.right)
            root.data = temp.data
            root.right = root.right.delete(temp.data)
        return root
