class Tree:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):
    if root is None:
        return
    print(root.data, end=":")
    if root.left is not None:
        print("L",root.left.data, end=" ")
    if root.right is not None:
        print("R",root.right.data,end="")
    print()
    printTree(root.left)
    printTree(root.right)


def TakeinputTree():
    rootdata = int(input())
    if rootdata ==-1:
        return None
    root = Tree(rootdata)
    lefttree = TakeinputTree()
    righttree = TakeinputTree()
    root.left = lefttree
    root.right = righttree
    return root


def numOfNode(root):
    if root is None:
        return 0
    return 1 + numOfNode(root.left) + numOfNode(root.right)

def removeleaves(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return None
    root.left = removeleaves(root.left)
    root.right = removeleaves(root.right)
    return root

def mirrorTree(root):
    if root is None:
        return
    left = mirrorTree(root.left)
    right = mirrorTree(root.right)
    root.left = right
    root.right = left
    return root

def Height(root):
    if root is None:
        return 0
    return 1+max(Height(root.left),Height(root.right))

def isBalanced(root): ### Time complexity O(n^2)
    if root is None:
        return True
    lf = Height(root.left)
    rf = Height(root.right)
    if lf-rf >1 or rf-lf >1:
        return False
    isLeftBalanced = isBalanced(root.left)
    isRightBalanced = isBalanced(root.right)
    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False


def getHeadandCheckBalanced(root):
    if root is None:
        return 0,True
    lh,isLeftBalanced = getHeadandCheckBalanced(root.left)
    rh,isRightBalanced = getHeadandCheckBalanced(root.right)
    h = 1+max(lh,rh)
    if lh-rh >1 or rh-lh >1:
        return h,False
    if isLeftBalanced and isRightBalanced:
        return h,True
    else:
        return h,False






#root = TakeinputTree()

printTree(root)
#print(getHeadandCheckBalanced(root))

#print("Number of node = ",numOfNode(root))
#root = removeleaves(root)
#printTree(root)
#root = mirrorTree(root)
#printTree(root)
