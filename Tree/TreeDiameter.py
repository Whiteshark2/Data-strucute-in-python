class Tree:

    def __init__(self,data):
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

def CreateTreeUsingInandPreorder(pre,inorder):
    if len(pre) ==0:
        return None
    rootdata = pre[0]
    root = Tree(rootdata)
    rootindexInOrder = -1
    for i in range(0,len(inorder)):
        if inorder[i]== rootdata:
            rootindexInOrder = i
            break
    if rootindexInOrder ==-1:
        return None
    leftinorder = inorder[0:rootindexInOrder]
    rightinoder = inorder[rootindexInOrder+1:]
    leftsubtree =len(leftinorder)
    leftpreorder = pre[1:leftsubtree+1]
    rightpreorder = pre[leftsubtree+1:]
    leftchild = CreateTreeUsingInandPreorder(leftpreorder,leftinorder)
    rightchild = CreateTreeUsingInandPreorder(rightpreorder,rightinoder)
    root.left = leftchild
    root.right = rightchild
    return root






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

"""def TakeinputTree():
    rootdata = int(input())
    if rootdata ==-1:
        return None
    root = Tree(rootdata)
    lefttree = TakeinputTree()
    righttree = TakeinputTree()
    root.left = lefttree
    root.right = righttree
    return root      """



def Height(root):
    if root is None:
        return 0
    return 1+max(Height(root.left),Height(root.right))

def DiameterOfTree(root):
    if root is None:
        return 0
    option1 = Height(root.left)+Height(root.right)
    option2 = DiameterOfTree(root.left)
    option3 = DiameterOfTree(root.right)
    return max(option3,option2,option1)

pre = [1,2,4,5,3,6,7]
inorder = [4,2,5,1,6,3,7]
root = CreateTreeUsingInandPreorder(pre,inorder)
printTree(root)