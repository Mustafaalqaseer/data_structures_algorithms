

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.rightChild = None 
        self.leftChild = None
        

def preOrderTraversal(rootNode):
    if not rootNode:
        return None   
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)       




newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild






#print(f"Initial Attributes: {whiskers.name}
#({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")   

preOrderTraversal(newBT)
         
