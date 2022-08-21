class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


import queue
def takeLevelwiseInput():
    q = queue.Queue()
    print("enter root")
    rootdata = int(input())
    if rootdata ==-1:
        return None
    root = Tree(rootdata)
    q.put(root)
    while not (q.empty()):
        currentNode = q.get()
        print("Enter the left child of ",currentNode.data)
        leftchildData = int(input())
        if leftchildData !=-1:
            leftchild = Tree(leftchildData)
            currentNode.left = leftchild
            q.put(leftchild)

        print("Enter the right child of ",currentNode.data)
        rightchildData= int(input())
        if rightchildData !=-1:
            rightchild = Tree(rightchildData)
            currentNode.right = rightchild
            q.put(rightchild)
    return root

def printTree(root):
    if root is None:
        return
    print(root.data, end=": ")
    if root.left is not None:
        print("L ", root.left.data, end=" ")
    if root.right is not None:
        print("R ",root.right.data, end = " ")
    print()
    printTree(root.left)
    printTree(root.right)


"""def insertion(root,x):
    if root is None:
        root = x
    left = insertion(root.left,x)
    return root"""

root = takeLevelwiseInput()
printTree(root)
