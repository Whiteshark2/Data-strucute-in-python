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

def Search(root,x):  ###### Binary Search Tree
    if root is None:
        return False
    if root.data == x:
        return True
    elif root.data < x:
        return Search(root.right,x)
    else:
        return Search(root.left,x)


def printDataBetweenK1andK2(root,k1,k2): #### Best For BST
    if root is None:
        return
    if root.data >k2:
        printDataBetweenK1andK2(root,k1,k2)
    elif root.data <k1:
        printDataBetweenK1andK2(root,k1,k2)
    else:
        print(root.data)
        printDataBetweenK1andK2(root.left,k1,k2)
        printDataBetweenK1andK2(root.right,k1,k2)


def printbetweenk1k2(root,k1,k2): ###### for Binary Tree
    if root is None:
        return
    if root.data >k1 and root.data <k2:
        print(root.data)
    printbetweenk1k2(root.left,k1,k2)
    printbetweenk1k2(root.right,k1,k2)

def CreateBstFromSortedArray(list):   ## Create BST from Array
    if len(list) == 0:
        return
    mid = len(list)//2
    root = Tree(list[mid])
    leftsubtree = CreateBstFromSortedArray(list[0:mid])
    rightsubtree = CreateBstFromSortedArray(list[mid+1:])
    root.left = leftsubtree
    root.right = rightsubtree
    return root


def createandInsertDuplicateNode(root):
    if root is None:
        return
    createandInsertDuplicateNode(root.left)
    createandInsertDuplicateNode(root.right)
    oldleft = root.left
    Duplicate = Tree(root.data)
    root.left = Duplicate
    Duplicate.left = oldleft
    return root


def minTree(root):
    if root is None:
        return 100000
    leftmin = minTree(root.left)
    rightmin = minTree(root.right)
    return min(leftmin,rightmin,root.data)

def maxTree(root):
    if root is None:
        return -100000
    leftmax = maxTree(root.left)
    rightmax = maxTree(root.right)
    return max(leftmax,rightmax,root.data)

def isBST(root):  ## O(n^2)
    if root is None:
        return True
    leftmax = maxTree(root.left)
    rightmin = minTree(root.right)
    if root.data <= leftmax or root.data >rightmin:
        return False
    isLeftBST = isBST(root.left)
    isRightBst = isBST(root.right)
    return isRightBst and isLeftBST


def isBST2(root):
    if root is None:
        return 100000,-100000,True
    leftmin,leftmax,isLeftBST = isBST2(root.left)
    rightmin,rightmax,isRightBST = isBST2(root.right)
    maximum = max(leftmax,rightmax,root.data)
    minimum = min(leftmin,rightmin,root.data)
    isBST = True
    if root.data >rightmin or root.data <=leftmax:
        isBST = False
    if not isLeftBST or not isRightBST:
        isBST = False
    return minimum,maximum,isBST

def isBST3(root,min,max):
    if root is None:
        return True
    if root.data <min or root.data >max:
        return False
    isLeftOk = isBST3(root.left,min,root.data -1)
    isRightOk = isBST3(root.right, root.data, max )
    return isLeftOk and isRightOk


def nodetoRootpath(root,s):
   if root is None:
       return None
   if root.data == s:
       l=list()
       l.append(root.data)
       return l
   leftoutput = nodetoRootpath(root.left,s)
   if leftoutput is not None:
       leftoutput.append(root.data)
       return leftoutput
   rightoutput = nodetoRootpath(root.right,s)
   if rightoutput is not None:
       rightoutput.append(root.data)
       return rightoutput
   else:
       return None


def nodeWithNosibling(root):
    if root is None:
        return
    if root.left is None and root.right is not None:
        print(root.right.data ,end="")
    elif root.left is not None and root.right is None:
        print(root.left.data ,end="")
    nodeWithNosibling(root.left)
    nodeWithNosibling(root.right)




root = takeLevelwiseInput()
printTree(root)
#print(Search(root,5))
#print("------------")
#print(printDataBetweenK1andK2(root,1,4))
#print(printbetweenk1k2(root,4,10))
#list = [1,2,3,4,5,6,7,8]
#root = CreateBstFromSortedArray(list)
print("-----------")
#root = createandInsertDuplicateNode(root))
#print(isBST3(root, float('-inf'), float('inf')))
#print(nodetoRootpath(root,5))
nodeWithNosibling(root)


