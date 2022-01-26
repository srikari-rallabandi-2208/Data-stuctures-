import snoop

class BinaryTreeNode:
    
    def __init__(self, data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

    def insert(self,data):
        if self.data:
            if self.data > data:
                if self.leftNode is None:
                    self.leftNode = BinaryTreeNode(data)
                else:
                    self.leftNode.insert(data)
            else:
                if self.rightNode is None:
                    self.rightNode = BinaryTreeNode(data)
                else:
                    self.rightNode.insert(data)
        else:
            self.data = data
    
    def print_tree(self):
        if self.leftNode:
            self.leftNode.print_tree()
        print(self.data)
        if self.rightNode:
            self.rightNode.print_tree()
    
    def is_sbt(self,root):
        if root.data is None or (root.leftNode is None and root.rightNode is None):
            return True
        if root.rightNode is None or root.leftNode is None:
            return False
        return self.is_sbt(root.leftNode) and self.is_sbt(root.rightNode)

    #@snoop
    def all_nodes_at_same_level(self,root,currentlevel,leaflevel):
        if root is None:
            return True
        # if you reach the leaf node
        if root.leftNode is None and root.rightNode is None:
            # if leaf level is not set set the leaf level
            if self.leaflevel == -1:
                self.leaflevel = currentlevel
                print(f"Setting leaf level to: {self.leaflevel}")
            elif currentlevel == self.leaflevel:
                return True
            else:
                return False
        return self.all_nodes_at_same_level(root.leftNode,currentlevel+1,self.leaflevel) and self.all_nodes_at_same_level(root.rightNode,currentlevel+1,self.leaflevel)
       
    def is_same_level(self,root):
        self.leaflevel = -1
        return self.all_nodes_at_same_level(root,0,self.leaflevel)

if __name__ == "__main__":
    
    root = BinaryTreeNode(20)
    root.insert(10)
    root.insert(30)
    root.insert(15)
    root.insert(7)
    
    root.print_tree()
    print(root.is_sbt(root.leftNode))
    print(root.is_same_level(root))
    root.insert(25)
    root.insert(35)
    print(root.is_same_level(root))
        
        