from node import Node

class Stack():

    def __init__(self):
        self.top = None
        self._size = 0
    

    def push(self,elem):
        """Insera um elemento na pilha"""
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size += 1



    def pop(self):
        """Remove um elemento da pilha"""
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        raise IndexError("The stack is empty.")

    
    def peek(self):
        """Retorna o topo da pilha"""
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty.")
    
    def __len__(self):
        """Retorna o tamanho da pilha"""
        return self._size
    

    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r+str(pointer.data) + "\n"
            pointer = pointer.next
        return r
    

    def __str__(self):
        return self.__repr__()

