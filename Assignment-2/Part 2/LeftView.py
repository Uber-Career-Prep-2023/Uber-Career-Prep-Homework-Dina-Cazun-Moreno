#Level Order (Breadth-First) Traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def leftViewUtil(root, level, max_level):
    if root is None:
        return

    if (max_level[0] < level):
        print (root.data, end = " ")
        max_level[0] = level
 
    leftViewUtil(root.left, level + 1, max_level)
    leftViewUtil(root.right, level + 1, max_level)
 
def leftView(root):
    max_level = [0]
    leftViewUtil(root, 1, max_level)
 
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(8)
    root.right.right = Node(15)
    root.right.left = Node(12)
    root.right.right.left = Node(14)
     
    print(leftView(root))
#Output: 10 2 7 14
