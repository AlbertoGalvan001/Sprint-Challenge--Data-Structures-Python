

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #take the current value of our node (self.value)
        # compare the new value we want to insert

        # if new value <= self.value
        if value < self.value:
           # if self.left is already taken by a node
           # make the left node call insert
           # set the left node to the new value
           if self.left is None:
               self.left = BSTNode(value)
           else:
               self.left.insert(value)     

        if value >= self.value:
            # If self.right is already taken by a node
           if self.right is None:
                #make that (right) node call insert
                self.right = BSTNode(value)
            # set the right child to the new node with the new value   
           else:
               self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current 'value < target
        found = False
        if self.value >= target:
            #check the left subtree (self.left.contains(target))
            # if you cannot go left, return false
            if self.left is None:
                return False  
            found = self.left.contains(target)  
            
        # if current value >= target
        if self.value < target:
            # check if right subtree contains target
            # if you cannot go right, return false    
            if self.right is None:
                return False
            found = self.right.contains(target)     

        return found

    # Return the maximum value found in the tree
    def get_max(self):
        # the largest value will always be to the right of the current node
        # if we can go right, find the largest number there by calling get_max on the right subtree.
        # if you can go right, return the current value.
        if self.right is None:
            return self.value
        return self.right.get_max()    
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call function on the current value fn(self.value)
        fn(self.value)
        # if you can go left, call for_each on the left tree
        if self.left:
            self.left.for_each(fn)
        # if you can go right, call for_each on the right tree
        if self.right:
            self.right.for_each(fn)