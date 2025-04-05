'''
    Hanna Syed
    Project 2
    Tree Index.py
'''

class TreeIndex:
    class Node:
        def __init__(self, payload, player):
            self.payload = payload
            self.player = player
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def add(self, payload, player):
        newnode = self.Node(payload, player)
        if self.root is None:
            self.root = newnode
        else:
            runner = self.root
            while True:
                if runner.payload > payload:
                    if runner.left is None:
                        runner.left = newnode
                        return
                    else:
                        runner = runner.left
                else:
                    if runner.right is None:
                        runner.right = newnode
                        return
                    else:
                        runner = runner.right

    def find(self, target, depth=0):
        if not self.find_helper(self.root, target, depth):
            print(target + " NOT FOUND anywhere!")

    def find_helper(self, somenode, target, depth):
        if somenode is None:
            return False
        if somenode.payload == target:
            print("Found " + target + " at node: " + str(id(somenode)) + " Depth: " + str(depth))
            return True
        elif somenode.payload > target:
            return self.find_helper(somenode.left, target, depth + 1)
        else:
            return self.find_helper(somenode.right, target, depth + 1)

    def print(self, showNones=False):
        self.print_helper(self.root, 0, showNones)

    def print_helper(self, somenode, indent, showNones):
        if somenode is None:
            return
        if somenode.right is None:
            if showNones:
                print(" " * (indent + 4) + "(NONE)")
        else:
            self.print_helper(somenode.right, indent + 4, showNones)
        print(" " * indent + str(somenode.payload))
        if somenode.left is None:
            if showNones:
                print(" " * (indent + 4) + "(NONE)")
        else:
            self.print_helper(somenode.left, indent + 4, showNones)
            
    def isleaf(somenode):
        return somenode.left is None and somenode.right is None



            
