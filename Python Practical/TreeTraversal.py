class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

""" def inputTree():
        rootdata = int(input())
        if rootdata ==-1:
            return None
        root = Tree(rootdata)
        leftTree = inputTree()
        rightTree = inputTree()
        root.left = leftTree
        root.right = rightTree
        return root"""

def printinorder(root):
        if root is None:
            return None
        left = printinorder(root.left)
        print(root.data)
        right = printinorder(root.right)

def printpostorder(root):
        if root is None:
            return None
        left = printpostorder(root.left)
        right = printpostorder(root.right)
        print(root.data)

def printpreorder(root):
        if root is None:
            return None
        print(root.data)
        left = printpreorder(root.left)
        right = printpreorder(root.right)

#root = inputTree()
a=Tree(1)
b=Tree(2)
c=Tree(3)
root=a
root.left=b
root.right=c
print("Printing preorder")
printpreorder(root)
print("Printing inorder")
printinorder(root)
print("Printing postorder")
printpostorder(root)









