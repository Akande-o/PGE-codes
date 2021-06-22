# Information can be found at https://cw.felk.cvut.cz/brute/data/ae/release/2021l_be5b33pge/pge2021/evaluation/input.php?task=LERtrees_py
import sys
import queue
import random
# This is to increase the maximum recursion limit which is set by python for larger data set
sys.setrecursionlimit(10**9)
class Node:
    """This object is to define each attribute of every node in a binary tree"""
    def __init__(self, key):
        self.key = key
        self.color = None
        self.left = None
        self.right = None
        self.parent = None
        self.xcoord = -1
        self.tag = ' ' # one character
        self.b = 0
        self.bb = 0
        self.w = 0
        self.ww = 0
class BinaryTree:
    """This object defines all we need to know about the binary tree"""
    def __init__(self, key ):
        self.root = Node(key)
    def setXcoord(self, node, x_coord):
        if node == None: return x_coord
        node.xcoord = self.setXcoord(node.left, x_coord) + 1
        #print(node.key, node.setXcoord)
        return self.setXcoord(node.right, node.xcoord)
    def countNodes(self, node):
        if node == None: return 0
        else:
            return node.key + self.countNodes( node.left ) + self.countNodes( node.right )

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
    def num_white(self, node):
        """This computes the number of white nodes within a binary tree"""
        if node is None:return 0           
        node.w = self.num_white(node.left)   
        node.ww = self.num_white(node.right)
        if node.color == 0:
            num = 1
        else:
            num = 0
        return num + node.w + node.ww
    
    def num_black(self, node):
        """This computes the number of black nodes within a binary tree"""
        if node is None:return 0
        node.b = self.num_black(node.left)
        node.bb = self.num_black(node.right)
        if node.color == 1:
            num = 1
        else:
            num = 0
        return num + node.b + node.bb

    def E(self, node):
        """Computes the total number of E-trees in a binary tree"""
        if node is None: return 0
        w = node.w
        ww = node.ww
        b = node.b
        bb = node.bb
        if w>0 and ww>0 and b>0 and bb>0 and (w/b) == (ww/bb):
            num = 1
        else:
            num = 0
        return num + self.E(node.left) + self.E(node.right)
    def R(self, node):
        """Computes the total number of R-trees in the binary tree"""
        if node is None: return 0
        w = node.w
        ww = node.ww
        b = node.b
        bb = node.bb
        if w>0 and ww>0 and b>0 and bb>0 and (w/b) < (ww/bb):
            num = 1
        else:
            num = 0
        return num + self.R(node.left) + self.R(node.right)
    def L(self, node):
        """Computes the total number of L-trees in the binary tree"""
        if node is None: return 0
        w = node.w
        ww = node.ww
        b = node.b
        bb = node.bb
        if w>0 and ww>0 and b>0 and bb>0 and (w/b) > (ww/bb):
            num = 1
        else:
            num = 0
        return num + self.L(node.left) + self.L(node.right)

# Initialising some parameters based on the input data
N = int(input())
color_nodes = list(map(int, input().split()))
t = BinaryTree(0)     # Creating the tree
tree_node = []         # initialising the list of nodes in the tree
tree_node.append(t.root)     # appending the root of the tree to the list of nodes on the tree
# Initialising all the nodes in the tree for easier preprocessing
for j in range(1, N):
    node = Node(j)
    tree_node.append(node)
# Preprocessing each node with the tree_node list as well as updating the tree with parent-child relationship defined
for i in range(N-1):
    node_list = list(map(int, input().split()))
    node_tuple = tuple(node_list)
    key, child, position = node_tuple  
    node = tree_node[key]    # extracting the data and updating the node object
    child_node = tree_node[child]     
    child_node.color = color_nodes[child]
    # Estabishing the parent-child relationship in the tree
    if position == 0:
        node.left = child_node   
    else:
        node.right = child_node
# Using a preliminary and predefined method to compute the total number of L-E-R trees in the binary tree
t.num_black(t.root)
t.num_white(t.root)
print(t.L(t.root), t.E(t.root), t.R(t.root))
