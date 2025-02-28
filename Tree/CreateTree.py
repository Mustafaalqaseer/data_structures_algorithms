


class TreeNode:
    def __init__(self,data,children = []):
        self.data = data
        self.children = children

    def __str__(self,level =0):
        res = '  ' * level + str(self.data) + '\n'
        for child in self.children:
            res += child.__str__(level + 1)
        return res 
    
    def addChild(self,treeNode):
        self.children.append(treeNode)


tree = TreeNode('Drinks', [])
cold = TreeNode('cold', [])
hot = TreeNode('hot', [])

cola = TreeNode('Cola', [])
lemonade = TreeNode('lemonada', [])
coffee = TreeNode("Coffee", [])
tea = TreeNode('Tea', [])



tree.addChild(cold)
tree.addChild(hot)
cold.addChild(cola)
cold.addChild(lemonade)
hot.addChild(coffee)
hot.addChild(tea)
print(tree)

