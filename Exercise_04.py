 #creating an empty node
class BTreeNode:
    def __init__(self, leaf = False):
        self.leaf = leaf
        self.keys = []
        self.children = []


 #tree
class ABtree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.height = t #it seems like it is the height of the tree

     #insert method
    def insert(self, k): #k for keys
        root = self.root
        if len(root.keys) == (2*self.height) - 1:
            temp = BTreeNode() #creating a temporary btree node
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)




