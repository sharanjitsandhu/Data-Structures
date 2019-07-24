class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 'insert' adds the input value to the binary search tree,
# adhering to the rules of the ordering of elements in a binary search tree.
    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTreeNode(value)
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTreeNode(value)

    # def insert(self, value):
    #     if value < self.value:
    #         if not self.left:
    #             self.left = BinarySearchTreeNode(value)
    #         else:
    #             # recursive to keep going until we find an empty spot
    #             self.left.insert(value)

    #     else:
    #         if not self.right:
    #             self.right = BinarySearchTreeNode(value)
    #         else:
    #             self.right.insert(value)

# 'contains' searches the binary search tree for the input value,
# returning a boolean indicating whether the value exists in the tree or not.
    def contains(self, target):
        if target == self.value:
            return True

        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False

# 'get_max' returns the maximum value in the binary search tree.
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

# for_each performs a traversal of every node in the tree,
# executing the passed-in callback function on each tree node value.
# There is a myriad(a lot) of ways to perform tree traversal;
# in this case any of them should work.
# This algo is recursive
# each time we'll be looking at the sub tree of the main tree.
    def for_each(self, cb):
      # in-order traversal(left, root, right)
        if self.left:
            self.left.for_each(cb)
        cb(self.value)
        if self.right:
            self.right.for_each(cb)

# tree = BinarySearchTreeNode(8)
# tree.insert(15)
# tree.insert(6)
# print(tree.left.value)
