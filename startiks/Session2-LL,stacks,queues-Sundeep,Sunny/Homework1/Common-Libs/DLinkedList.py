class Node():
    def __init__(self, next_node=None, previous_node=None, data=None):
        self.next_node = next_node
        self.previous_node = previous_node
        self.data = data

class DLList():
    def __init__(self):

        self.first_node = None
        self.last_node = None

    def push(self,data):
        node = Node()
        if self.first_node == None :
            node.data = data
            node.previous_node = None
            node.next_node = None
            self.first_node = node
            self.last_node =  node
        else:
            node.data = data
            node.next_node = self.first_node
            node.previous_node = None
            self.first_node.previous_node =node
            self.first_node =node
        return(self.first_node)

    def push_front(self, node):
        '''Pushes the node <node> at the "front" of the ll
        '''
        node.next_node = self.first_node
        node.previous_node = None
        self.first_node.previous_node = node
        self.first_node = node

    def pop(self):
        '''Pops the last node out of the list'''
        data = self.last_node.data
        old_last_node = self.last_node
        to_be_last = self.last_node.previous_node
        to_be_last.next_node = None
        old_last_node.previous_node = None

        # Set the last node to the "to_be_last"
        self.previous_node = to_be_last

        return data

    def remove(self, node):
        '''Removes and returns node, and connects the previous and next
        nicely
        '''
        next_node = node.next_node
        previous_node = node.previous_node

        previous_node.next_node = next_node
        next_node.previous_node = previous_node

        # Make it "free"
        node.next_node = node.previous_node = None

        return node

    def __str__(self):
        next_node = self.first_node
        s = ""
        while next_node:
            s += str(next_node.data) + ","
            next_node = next_node.next_node

        return s
