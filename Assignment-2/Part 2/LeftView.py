#Level Order (Breadth-First) Traversal

class BinarySearchTree:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

    def leftView(root):
        if not root:
            return
    
        arr = []
        arr.append(root)

        while(len(arr)):
            num = len(arr)

            for i in range(1, num + 1):
                temp = arr[0]
                arr.pop(0)

                if i == 1:
                    print(temp.data, end = "")

                if temp.left != None:
                    arr.append(temp.left)

                if temp.right != None:
                    arr.append(temp.right)
