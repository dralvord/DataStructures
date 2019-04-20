from BinarySearchTree import BinarySearchTree
from BinarySearchTree import Tree


class RBTree(Tree):
    def __init__(self,data):
        Tree.__init__(self, data)
        self.parent = None
        self.red = True
        
class RedBlackBST(BinarySearchTree):
    def __init__(self):
        BinarySearchTree.__init__(self)
    
    #-------------------------------Insert----------------------------------------
    def Insert(self, data):
        if self.root == None:
            newTree = RBTree(data)
            newTree.red = False
            self.root = newTree
            
        else: 
            self.InsertNode(self.root,data,None)
        
    def InsertNode(self,currentNode, data, parent):
        if currentNode.data < data:
            if currentNode.right == None:
                newTree = RBTree(data)
                currentNode.right = newTree
                currentNode.right.parent = parent
                self.BalanceTree(currentNode)
            else:
                self.InsertNode(currentNode.right, data, currentNode)
        elif currentNode.data > data:
            if currentNode.left == None:
                newTree = RBTree(data)
                currentNode.left = newTree
                currentNode.left.parent = parent
                self.BalanceTree(currentNode)
            else:
                self.InsertNode(currentNode.left, data, currentNode)
        else:
            print("Duplicate Data.")
    
    #----------------------------Balance Tree-----------------------------------
    
    def BalanceTree(self, currentNode):
        "Restore red-black properties after insert."
        while currentNode.parent != None and currentNode.parent.red:
            if currentNode.parent.parent != None and currentNode.parent.parent.left != None and currentNode.parent.parent.right != None and currentNode.parent == currentNode.parent.parent.left:
                y = currentNode.parent.parent.right
                if y.red:
                    currentNode.parent.red = False
                    y.red = False
                    currentNode.parent.parent.red = True
                    currentNode = currentNode.parent.parent
                else:
                    if currentNode == currentNode.parent.right:
                        currentNode = currentNode.parent
                        self.RotateLeft(currentNode)
                    currentNode.parent.red = False
                    currentNode.parent.parent.red = True
                    self.RotateRight(currentNode.parent.parent)
            elif currentNode.parent.parent != None and currentNode.parent.parent.left != None and currentNode.parent.parent.right != None:
                y = currentNode.parent.parent.left
                if y.red:
                    currentNode.parent.red = False
                    y.red = False
                    currentNode.parent.parent.red = True
                    currentNode = currentNode.parent.parent
                else:
                    if currentNode == currentNode.parent.left:
                        currentNode = currentNode.parent
                        self.RotateRight(currentNode)
                    currentNode.parent.red = False
                    currentNode.parent.parent.red = True
                    self.RotateLeft(currentNode.parent.parent)
            else:
                currentNode = currentNode.parent
        self.root.red = False
    
    #----------------------Rotate Left----------------------------    
    def RotateLeft(self, currentNode):
        print("In RotateLeft")
        sibling = currentNode.right
        currentNode.right = sibling.left
        
        if sibling.left != None:
            sibling.left.parent = currentNode
        sibling.parent = currentNode.parent
        if currentNode.parent == None:
            self.root = sibling
        else:
            if currentNode == currentNode.parent.left:
                currentNode.parent.left = sibling
            else:
                currentNode.parent.right = sibling
        sibling.left = currentNode
        currentNode.parent = sibling
    
    #---------------------Rotate Right-------------------------------    
    def RotateRight(self, currentNode):
        print("In RotateRight")
        sibling = currentNode.left
        currentNode.left = sibling.right
        
        if sibling.right != None:
            sibling.right.parent = currentNode
        sibling.parent = currentNode.parent
        if currentNode.parent == None:
            self.root = sibling
        else:
            if currentNode == currentNode.parent.right:
                currentNode.parent.right = sibling
            else: 
                currentNode.parent.left = sibling
        sibling.right = currentNode
        currentNode.parent = sibling
        
    #----------------------Find------------------------------
    def Find(self,data):
        BinarySearchTree.Find(self, data)
        
    #-------------------Print Methods--------------------------
    def PrintAscending(self):
        BinarySearchTree.PrintAscending(self)
        
    def PrintDescending(self):
        BinarySearchTree.PrintDescending(self)
        
    def PrintRoot(self):
        print(self.root.data)
        