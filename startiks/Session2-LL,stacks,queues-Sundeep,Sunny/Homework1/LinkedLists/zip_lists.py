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



        # Complete the function below.


# For your reference:
# LinkedListNode {
#    int val
#    LinkedListNode next
# }

def Zip():

    my_plist = LinkedList()
    my_array = [5,8,34,66,43,8888]
    for num in  (my_array):
        my_plist.insert_at_tail(num)
        #pList = pList.next
    size = my_plist.size()
    print("Before Zip size is %s", size)
    my_plist.printList()
    size_half = int(size / 2)
    # break the linked lists into 2
    count = 0
    my_flist = LinkedList()
    my_slist = LinkedList()
    list_itr = my_plist.head
    while (count < size):
        if count < size_half:
            if list_itr:
                my_flist.insert_at_tail(list_itr.val)
        else:
            if list_itr:
                my_slist.insert_at_head(list_itr.val)
        list_itr = list_itr.next
        count = count + 1
    print("First List \n")
    my_flist.printList()
    print("Second List \n")
    my_slist.printList()
    my_ziplist = LinkedList()
    my_flist_c = my_flist.head
    my_slist_c = my_slist.head
    while (my_flist_c or my_slist_c):
        if (my_flist_c):
            my_ziplist.insert_at_tail(my_flist_c.val)
            my_flist_c = my_flist_c.next
        if (my_slist_c):
            my_ziplist.insert_at_tail(my_slist_c.val)
            my_slist_c = my_slist_c.next
    print("Zip List \n")
    my_ziplist.printList()


Zip()

