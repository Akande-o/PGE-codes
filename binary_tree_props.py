#Information can be found at https://cw.felk.cvut.cz/brute/data/ae/release/2021l_be5b33pge/pge2021/evaluation/input.php?task=treeproperties
import random
import queue

class Node:
    """This object deals with each node in the binary tree"""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.xcoord = -1
        self.tag = ' ' # one character
        self.balance = 0
        self.count_only_left = 0
        self.count_only_right = 0
        self.minimal = 0
        self.maxleaf = 0
        self.nodes2L = 0
        self.nodes2R = 0
        self.num = 0



    def print(self):
        print( "[" + str(self.key) + "]", end = "" )
        print( str(self.xcoord)+", ", end = "")

class BinaryTree:
    """This object deals with the binary tree as a whole"""
    def __init__(self, key ):
        self.root = Node( key )

    def setXcoord(self, node, x_coord):
        if node == None: return x_coord
        node.xcoord = self.setXcoord(node.left, x_coord) + 1
        #print(node.key, node.setXcoord)
        return self.setXcoord(node.right, node.xcoord)

    def countNodes(self, node):
        if node == None: return 0
        else:
            return node.key + self.countNodes( node.left ) + self.countNodes( node.right )

    def numberOfNodes(self, node):
        if node == None: return 0
        else:
            return 1 + self.numberOfNodes( node.left ) + self.numberOfNodes( node.right )

    def display(self):
        self.setXcoord(self.root, 0)
        qu = queue.Queue()
        prevDepth = -1
        prevEndX = -1
        # in the queue store pairs(node, its depth)
        qu.put( (self. root, 0) )
        while not qu.empty():
            node, nodeDepth = qu.get()

            LbranchSize = RbranchSize = 0
            if node.left != None:
                LbranchSize = (node.xcoord - node.left.xcoord)
                qu.put( (node.left, nodeDepth+1) )
            if node.right != None:
                RbranchSize = (node.right.xcoord - node.xcoord)
                qu.put( (node.right, nodeDepth+1) )

            LspacesSize = (node.xcoord - LbranchSize) - 1  # if first on a line
            if prevDepth == nodeDepth:                  # not first on line
                LspacesSize -= prevEndX

            # print the node, branches, leading spaces
            if prevDepth < nodeDepth and prevDepth > -1 : print() # next depth occupies new line
            nodelen = 3
            print( " "*nodelen*LspacesSize, end = '' )
            print( "_"*nodelen*LbranchSize, end = ''  )
            #print( "." + ("%2d"%node.key) + node.tag+".", end = '' )
            print( node.tag + ("%2d"%node.key), end = ''  )
            print( "_"*nodelen*RbranchSize, end = ''  )

            # used in the next run of the loop:
            prevEndX = node.xcoord + RbranchSize
            prevDepth = nodeDepth
        # end of queue processing

        N = self.countNodes( self.root )
        print("\n"+ '-'*N*nodelen) # finish the last line of the tree

    def count_2nodesL(self, node):
        if node == None: return 0
        if node.left != None and node.right != None:
            # print( " node with 2 children, key:", node.key)
            num = 1
        else:
            num = 0
        node.parent.nodes2L = 1 + self.count_2nodesL(node.left) + self.count_2nodesL(node.right)
        return node.parent.nodes2L
    def count_2nodesR(self, node):
        if node == None: return 0
        if node.left != None and node.right != None:
            # print( " node with 2 children, key:", node.key)
            num = 1
        else:
            num = 0
        node.parent.nodes2R = num + self.count_2nodesR(node.left) + self.count_2nodesR(node.right)
        return node.parent.nodes2R
    def node_keys(self, SR, AL, AR, C0, CL, CR, D, depth, M, node):
        """Creates and adds each child to the current parent in a recursive fashion"""
        RK = node.key
        if SR < C0 or depth == D:
            self.leaves.append(RK)
            return False
        elif CR <= SR < M:
            left_key = (AL*(RK+1))%M
            left_SR = (SR * AL)%M
            node.left = Node(left_key)
            node.left.parent = node
            right_key = (AR*(RK+2))%M
            right_SR = (SR * AR)%M
            node.right = Node(right_key)
            node.right.parent = node
            self.node_keys(left_SR, AL, AR, C0, CL, CR, D, depth+1, M, node.left)
            self.node_keys(right_SR, AL, AR, C0, CL, CR, D, depth+1, M, node.right)
            return True
        elif CL <= SR < CR:
            right_key = (AR*(RK+2))%M
            right_SR = (SR * AR)%M
            node.right = Node(right_key)
            node.right.parent = node
            self.node_keys(right_SR, AL, AR, C0, CL, CR, D, depth+1, M, node.right)
            return True
        elif C0 <= SR < CL:
            left_key = (AL*(RK+1))%M
            left_SR = (SR * AL)%M
            node.left = Node(left_key)
            node.left.parent = node
            self.node_keys(left_SR, AL, AR, C0, CL, CR, D, depth+1, M, node.left)
            return True
        else:
            return False
    def cost(self, node, depth):
        """Computes the cost of the entire binary tree"""
        if node == None:
            return 0
        return node.key*(depth+1) + self.cost(node.left, depth+1) + self.cost(node.right, depth + 1)
    def disbalance(self, node):
        """Computes the disbalance of each node"""
        if node == None: return 0
        dis_left = self.disbalance(node.left)
        dis_right = self.disbalance(node.right)
        balance = abs(dis_left - dis_right)
        node.balance = balance
        return node.key + dis_left+ dis_right
    def disbalance2(self, node):
        """Computes the disbalance of the binary tree"""
        if node == None: return 0
        return node.balance + self.disbalance2(node.left) + self.disbalance2(node.right)
    def count_2nodes3(self, node):
        """Computes the number of nodes with 2 children within both left and right subtrees as well as comparing
        their equality within the binary tree"""
        if node == None: return False
        left2nodes = self.count_2nodes3(node.left)
        right2nodes = self.count_2nodes3(node.right)
        if node.left != None and node.right != None :
            num = 1
        else:
            num = 0
        if left2nodes == right2nodes:
            if node.left != None and node.right != None and left2nodes == 0:
                node.num = 1
            elif left2nodes == 0:
                node.num = 0
            elif left2nodes ==1:
                node.num =1
            else:
                node.num = 1
        else:
            node.num = 0
        return num + left2nodes + right2nodes
        
    def two_balanced3(self, node):
        """Computes the total number of two-balanced nodes(nodes with the same number of nodes with 2 children in both
        left and right subtrees of the n-tree)"""
        if node is None: return 0
        if node.num == 1:
            key = node.key
        elif node.num == 0:
            key = 0
        elif node.left != None and node.right != None:
            ChildL = node.left
            ChildR = node.right
            if ChildL.left == ChildL.right == None and ChildR.left == ChildR.right == None:
                key = node.key
            else:
                key = 0
        if node.left == node.right == None:
            key = node.key
        return key + self.two_balanced3(node.left) + self.two_balanced3(node.right)
    def parity(self, node):
        """Computes the parity of the binary tree (the total number of nodes with both children having the same remainder
        once divided by 2)"""
        if node == None: return 0
        if node.left == None or node.right == None:
            num = 0
        if node.left != None and node.right != None:
            if node.left.key%2 == node.right.key%2:
                num = 1
            else:
                num = 0
        return num + self.parity(node.left) + self.parity(node.right)
    def find_min_in_BT(self, node):
        """Computes the minimum node key in the entire binary tree"""
        if node is None:
            return 10**6
        res = node.key
        lres = self.find_min_in_BT(node.left)
        rres = self.find_min_in_BT(node.right)
        if lres < res:
            res = lres
        if rres < res:
            res = rres
        node.minimal = res
        return node.minimal
    def local_minimal(self, node):
        """Computes the sum of all local minimal nodes within each n-tree in the entire binary tree"""
        if node == None: return 0
        elif node.left == node.right == None:
            key = node.key
        elif node.key == node.minimal:
            key = node.key
        else:
            key = 0
        if node.left != None: key += self.local_minimal(node.left)
        if node.right != None: key += self.local_minimal(node.right)
        return key

    def n_leaves(self, node):
        """Produces the maximum node key which is a leaf in the binary tree"""
        if node == None: return 0
        if node.left == node.right == None:
            max_leaf = node.key
        else:
            max_leaf = 0
        lres = self.n_leaves(node.left)
        rres = self.n_leaves(node.right)
        if lres > max_leaf:
            max_leaf = lres
        if rres > max_leaf:
            max_leaf = rres
        node.maxleaf = max_leaf
        return node.maxleaf

    def weakly_dominant(self, node):
        """Computes the number of weakly dominant nodes in the entire binary tree"""
        if node is None: return 0
        if node.left == node.right == None:
            num = 0
        elif node.key >= node.maxleaf:
            num = 1
        else:
            num = 0
        if node.left != None: num += self.weakly_dominant(node.left)
        if node.right != None: num += self.weakly_dominant(node.right)
        return num

    def only_left(self, node):
        """Computes the number of nodes with only left children in the binary tree"""
        if node is None: return 0
        if node.left != None and node.right == None:
            num = 1
        else:
            num = 0
        node.count_only_left =  num + self.only_left(node.left)+ self.only_left(node.right)
        return node.count_only_left

    def only_right(self, node):
        """Computes the number of nodes with only right children in the binary tree"""
        if node is None: return 0
        if node.left == None and node.right != None:
            num = 1
        else:
            num = 0
        node.count_only_right = num + self.only_right(node.left)+ self.only_right(node.right)
        return node.count_only_right
    def L1_tree_version_2(self, node):
        """Computes the number of L1-trees in the binary tree (the number of n-trees which the subtree has at least
        one node with just a left child but no node with just a right child)"""
        if node == None: return 0
        if node.count_only_left > 0 and node.count_only_right == 0:
            num = 1
        else:
            num = 0
        if node.left != None:  num += self.L1_tree_version_2(node.left)
        if node.right != None: num += self.L1_tree_version_2(node.right)
        return num

    def increasing_path(self, node, path, lst):
        """Computes the every possibility of an increasing path in a binary tree"""
        if node == None:
            lst.append(path)
            path = 0
            return False
        elif node.parent != None and node.parent.key > node.key:
            lst.append(path)
            path = node.key
            self.increasing_path(node.left, path, lst)
            self.increasing_path(node.right, path, lst)
            return True
        elif node.left != None and node.right == None and node.key <= node.left.key:
            path += node.key
            self.increasing_path(node.left, path, lst)
            self.increasing_path(node.right, path, lst)
            return True
        elif node.right != None and node.left == None and  node.key <=node.right.key:
            path += node.key
            self.increasing_path(node.right, path,  lst)
            self.increasing_path(node.left, path, lst)
            return True

        elif node.right == node.left == None and node.parent.key <= node.key:
            path += node.key
            self.increasing_path(node.left, path, lst)
            self.increasing_path(node.right, path, lst)
        elif node.left != None and node.right != None and node.key <= node.left.key and node.key > node.right.key:
            path += node.key
            self.increasing_path(node.left, path, lst)
            self.increasing_path(node.right, path, lst)
            return True
        elif node.right != None and node.left != None and  node.key <=node.right.key and node.key > node.left.key:
            path += node.key
            self.increasing_path(node.right, path,  lst)
            self.increasing_path(node.left, path, lst)
            return True
        elif node.right != None and node.left != None and  node.key <=node.right.key and node.key <= node.left.key:
            path += node.key
            self.increasing_path(node.right, path,  lst)
            self.increasing_path(node.left, path, lst)
            return True
        elif node.right != None and node.left != None and  node.key > node.right.key and node.key > node.left.key:
            lst.append(path)
            path += node.key
            self.increasing_path(node.right, path,  lst)
            self.increasing_path(node.left, path, lst)
            return True
        else:
            lst.append(path)
            path += node.key
            self.increasing_path( node.left, path, lst)
            self.increasing_path(node.right, path,  lst)
            return True
    def max_path(self, node):
        """Returns the maximum increasing path in the binary tree"""
        lst = []
        path = 0
        self.increasing_path(node, path, lst)
        max_increase = max(lst)
        return max_increase

# initialising some parameters based on the input data available
initial = list(map(int, input().split()))
AL, AR, C0, CL, CR, D, M, RK, RSR = initial
depth = 0
# Creating the binary tree using the root key
t = BinaryTree( RK )
# Updating the binary tree based on the conditions given
t.node_keys(RSR, AL, AR, C0, CL, CR, D, depth, M, t.root)

#t.display()           # uncomment for trees with small depth for the visual display
# Using a predefined method to compute the cost
print(t.cost(t.root, 0))         #1
# Using a preliminary and predefined method to compute the sum of the disbalance of the binary tree
t.disbalance(t.root) 
print(t.disbalance2(t.root))      #2
# Using a preliminary and predefined method to compute the total number of two-balanced nodes in the binary tree
t.count_2nodes3(t.root)
print(t.two_balanced3(t.root))    #3
# Using a predefined method to compute the sum of all nodes with equal parity
print(t.parity(t.root))           #4
# Using a preliminary and predefined method to compute the sum of the local minimal nodes of the binary tree
t.find_min_in_BT(t.root)
print(t.local_minimal(t.root))        #5
# Using a preliminary and predefined method to compute the sum of the weakly dominant nodes of the binary tree
t.n_leaves(t.root)
print(t.weakly_dominant(t.root))      #6
# Using two preliminary and predefined method to compute the number of L1-trees in the binary tree
t.only_left( t.root )
t.only_right( t.root )
print( t.L1_tree_version_2(t.root) )           #7
# Using a predefined method to compute the maximum increasing path of the binary tree
print(t.max_path(t.root))
