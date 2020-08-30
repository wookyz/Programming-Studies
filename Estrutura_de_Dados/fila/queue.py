from node import Node

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0
    

    def push(self,elem):
        """Insera um elemento na fila"""
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        if self.first is None:
            self.fist = node
        
        self._size += 1


    def pop(self):
        """Remove um elemento da fila"""
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self._size -= 1
            return elem
        raise IndexError("The queue is empty")
    
    def peek(self):
        """Retorna o topo da fila"""
        if len(self) > 0:
            elem = self.first.data
            return elem
        raise IndexError("The queue is empty")
    
    def __len__(self):
        """Retorna o tamanho da fila"""
        return self._size
    

    def __repr__(self):
        if len(self)> 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r+str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "Empty Queue"
        

    def __str__(self):
        return self.__repr__()