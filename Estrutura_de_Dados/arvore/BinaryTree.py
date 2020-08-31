from node import Node
from queue import Queue

ROOT = "root"
class BinaryTree():
    
    def __init__(self,data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def inorder_traversal(self,node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)


    def postorder_traversal(self,node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)


    def preorder_traversal(self,node=None):
        if node is None:
            node = self.root
        print(node, end=" ")
        if node.left:
            self.preorder_traversal(node.left)
        if node.right:
            self.preorder_traversal(node.right)

    
    def height(self,node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft


    def levelorder_traversal(self,node=ROOT):   
        if node == ROOT:
            node = self.root

        queue = Queue()
        queue.push(node)
        while len(queue):
            queue.pop()
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
            print(node, end=" ")