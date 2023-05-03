class BinarySearchTree:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

    global floor

    def floorInBSTHelper(root, target):
        while root:
            if root.data == target:
                floor = root.data
            if target > root.data:
                floor = root.data
                root = root.right
            else:
                root = root.left

    def floorInBST(root, target):
        floor -= 1
        floorInBSTHelper(root, target)
        print(target, floor)
