class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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


def postorder(root):
    if root is None:
        return
    left = postorder(root.left)
    right = postorder(root.right)
    print(root.data)

def inorder(root):
    if root is None:
        return
    left = inorder(root.left)
    print(root.data)
    right = inorder(root.right)

def inputTree():
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = Tree(rootdata)
    lefttree = inputTree()
    righttree = inputTree()
    root.left = lefttree
    root.right = righttree
    return root

def numnode(root):
    if root is None:
        return 0
    leftcount = numnode(root.left)
    rightcount = numnode(root.right)
    return 1 + leftcount+rightcount

def sumofnode(root):
    if root is None:
        return 0
    sum = root.data
    leftsum = sumofnode(root.left)
    rightsum = sumofnode(root.right)
    return sum+leftsum+rightsum

def largestdata(root):
    if root is None:
        return -1 #Ideally would have returned -Infinity
    leftlargest = largestdata(root.left)
    rightlargest = largestdata(root.right)
    return max(leftlargest,rightlargest,root.data)

def heightofTree(root):
    if root is None:
        return 0
    leftheight = heightofTree(root.left)
    rightheight = heightofTree(root.right)
    return 1+ max(leftheight,rightheight)

def numberofLeaf(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    left = numberofLeaf(root.left)
    right = numberofLeaf(root.right)
    return right+left

def greaterThanX(root,x):
    if root is None:
        return 0
    if root.data > x:
        return 1
    greaterThanX(root.left,x)
    greaterThanX(root,x)
    return

"""def printNodeAtKdepth(root,k):
    if root is None:
        return
    if k==0:
        print(root.data)
        return
    printNodeAtKdepth(root.left,k-1)
    printNodeAtKdepth(root.right,k-1)"""

def printNodeAtKdepth1(root,k,d):
    if root is None:
        return
    if k==d:
        print(root.data)
        return
    printNodeAtKdepth1(root.left,k,d+1)
    printNodeAtKdepth1(root.right,k,d+1)

def isPresent(root,x):
    if root is None:
        return False
    if root.data == x:
        return True
    isPresent(root.left,x)
    isPresent(root.right,x)

root = inputTree()
printTree(root)
#print("Number of node = ", numnode(root))
#print("sum of node = ", sumofnode(root))
postorder(root)
#inorder(root)
#print("Largest data =" ,largestdata(root))
#print("Height of Tree = ",heightofTree(root))
#print("Number of leaf = ", numberofLeaf(root))
#print(greaterThanX(root,2))
#print(printNodeAtKdepth(root,1))
#print(isPresent(root,4))
#print(printNodeAtKdepth1(root,2,0))

