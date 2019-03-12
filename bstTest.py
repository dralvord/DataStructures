from BinarySearchTree import BinarySearchTree

bst = BinarySearchTree()

print("Inserting Values into Binary Search Tree")
bst.Insert(100)
bst.Insert(50)
bst.Insert(150)
bst.Insert(25)
bst.Insert(75)
bst.Insert(125)
bst.Insert(175)

print("Insertion Successful!")

print("Binary Search Tree in Ascending Order:")
bst.PrintAscending()
print("Binary Search Tree in Descending Order:")
bst.PrintDescending()

print("Searching for 100 in BST:")
if bst.Find(100):
    print("100 found in BST. Test successful")
else:
    print("Test failed")

print("Searching for 125 in BST:")
if bst.Find(125):
    print("125 found in BST. Test successful")
else:
    print("Test failed")
    
print("Deleting 100 from BST:")
bst.Delete(100)
if bst.Find(100):
    print("Delete unsuccessful. Test Failed")
else:
    print("Delete successful!")
    
print("Deleting 50 from BST:")
bst.Delete(50)
if bst.Find(50):
    print("Delete unsuccessful. Test Failed")
else:
    print("Delete successful!")
    
print("Deleting 175 from BST:")   
bst.Delete(175)
if bst.Find(175):
    print("Delete unsuccessful. Test Failed")
else:
    print("Delete successful!")
    
print("Binary Search Tree in Ascending Order:")
bst.PrintAscending()