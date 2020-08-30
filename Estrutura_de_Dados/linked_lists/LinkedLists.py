class Node():

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self, value):
        """Adiciona um elemento ao final da lista."""
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(value)
        else:
            self.head = Node(value)
        self._size += 1
    

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size
    

    def _getnode(self,index):
        """Retorna o nó da lista."""
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    
    def __getitem__(self,index):
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")


    def __setitem__(self,index, value):
        pointer = self._getnode(index)
        if pointer:
            pointer.data = value
        else:
            raise IndexError("list index out of range")


    def index(self,value):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == value:
                return i
            pointer = pointer.next
            i += 1
        raise IndexError("list index out of range")


    def insert(self,index,value):
        node = Node(value)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1


    def remove(self,value):
        if self.head.data == None:
            raise IndexError("{} is not in the list.".format(value))
        elif self.head.data == value:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == value:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size -= 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError("{} is not in the list.".format(value))



if __name__ == '__main__':
    # sequencial = []
    # sequencial.append(7)
    lista = LinkedList()
    lista.append(7)
    lista.append(80)
    lista.append(56)
    lista.append(32)
    lista.append(17)
    lista.insert(5,2)
    
    print(lista[5])

    lista.remove(2)

    print(lista[5])