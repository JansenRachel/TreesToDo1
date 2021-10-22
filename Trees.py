

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    

class BST:
    def __init__():
        self.root = None
    

#   Create an add(val) method on the BST object to add new value to the tree
    # def add(self, val):
    #     new_node = Node(val)
    #     if self.root == None:
    #         self.root = new_node
    #         return self
    #     runner = self.root
    #     while runner != None:
    #         if val <= runner.value:
    #             if runner.left == None:
    #                 runner.left = new_node
    #             runner = runner.left
    #         else:
    #             if runner.right == None:
    #                 runner.right = new_node
    #             runner = runner.right
    #     return self
    
    def add(self, val):
        if val == self.val:
            return
        if val < self.val:
            if self.left:
                self.left.add(val)
            else:
                self.left=BST(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = BST(val)


#   Create a contains(val) method on BST that returns whether the tree contains a given value
    def contains(self, val):
        if val == self.val:
            return True
        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

#   Create a min() method on the BST class that returns the smallest value found in the BST
    def min(self):
        current = self
        while current.left != None:
            current = current.left
        return current.val

#   Create a max() BST method that returns the largest value contained in the binary search tree
    def max(self):
        current = self
        while current.right != None:
            current = current.right
        return current.val


    # def PrintTree(self):
    #     if self.left:
    #         self.left.PrintTree()
    #     print( self.data),
    #     if self.right:
    #         self.right.PrintTree()



# bst=BST(5)
bst=BST(5)
bst.add(2)
bst.add(6)
bst.add(1)
bst.add(8)
print(bst.value)



