class Tree:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    #--------------------Insert Method-----------------------
    def Insert(self, data):
        if self.root == None:
            newTree = Tree(data)
            self.root = newTree
            
        else: 
            self.InsertNode(self.root,data)
    
    def InsertNode(self, currentNode, data):
        if currentNode.data < data:
            if currentNode.right == None:
                newTree = Tree(data)
                currentNode.right = newTree
            else:
                self.InsertNode(currentNode.right, data)
        elif currentNode.data > data:
            if currentNode.left == None:
                newTree = Tree(data)
                currentNode.left = newTree
            else:
                self.InsertNode(currentNode.left, data)
        else:
            print("Duplicate Data.")
    
    #---------------------Find Method----------------------        
    def Find(self, data):
        return self.FindNode(self.root, data)
        
    def FindNode(self, currentNode, data):
        if currentNode == None:
            return False
        elif data == currentNode.data:
            return True
        elif data > currentNode.data:
            return self.FindNode(currentNode.right, data)
        else:
            return self.FindNode(currentNode.left, data)
     
     
     #--------------------Delete Method---------------------
    def Delete(self, data):
        if self.root != None:
            self.DeleteNode(self.root, data)
    
    def DeleteNode(self, currentNode, data):
        if data < currentNode.data:
            currentNode.left = self.DeleteNode(currentNode.left, data)
        elif data > currentNode.data:
            currentNode.right = self.DeleteNode(currentNode.right, data)
        else:
            if currentNode.left == None:
                temp = currentNode.right
                currentNode = None
                return temp
            elif currentNode.right == None:
                temp = currentNode.left
                currentNode = None
                return temp
            
            temp = self.FindMinValNode(currentNode.right)
            
            currentNode.data = temp.data
            
            currentNode.right = self.DeleteNode(currentNode.right, temp.data)
            
        return currentNode    
    
    #---------------Find Min Helper for Delete--------------------        
    def FindMinValNode(self, currentNode):
        while(currentNode.left != None):
            currentNode = currentNode.left
        return currentNode
      
    #-------------------------Print Methods---------------------        
    def PrintAscending(self):
        self.PA(self.root)
    
    def PA(self,currentNode):
        if currentNode.left != None:
            self.PA(currentNode.left)
            
        print(currentNode.data)
        
        if currentNode.right != None:
            self.PA(currentNode.right)
    
            
    def PrintDescending(self):
        self.PD(self.root)
    
    def PD(self,currentNode):
        if currentNode.right != None:
            self.PD(currentNode.right)
            
        print(currentNode.data)
        
        if currentNode.left != None:
            self.PD(currentNode.left)