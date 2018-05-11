class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_at_tail(self, val):
        if self.head == None:
            self.head = LinkedListNode(val)
            self.tail = self.head
        else:
            node = LinkedListNode(val)
            self.tail.next = node
            self.tail = self.tail.next
            #        return self.tail

    def insert_at_head(self, value):
        new_node = LinkedListNode(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            #       return self.head

    def reverse(self):
        rList = LinkedListNode(self.head.val)
        current = self.head
        while (current):
            rList.insert_at_head(current.val)
            current = current.next
        return (rList)

    def printList(self):
        current = self.head
        while (current):
            print(current.val)
            current = current.next

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

def find_middle():
    my_plist = LinkedList()
    my_array = [5, 8, 34, 66, 43]
    for num in (my_array):
        my_plist.insert_at_tail(num)
    fast_ptr = my_plist.head
    slow_ptr = my_plist.head
    while(fast_ptr) :
        if fast_ptr.next != None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        else:
            fast_ptr = None
    print(slow_ptr.val)


find_middle()