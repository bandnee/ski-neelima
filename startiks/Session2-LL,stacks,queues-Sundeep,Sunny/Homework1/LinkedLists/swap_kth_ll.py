# Complete the function below.

# For your reference:
# LinkedListNode {
#    int val
#    LinkedListNode next
# }

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
        print("Size:", count)
        return count


def swapNodes(pList, k):
    my_plist = LinkedList()
    # my_array = [5,8,34,66,43,8888]
    # for num in  (my_array):
    while (pList):
        # my_plist.insert_at_tail(num)
        my_plist.insert_at_tail(pList.val)
        pList = pList.next
    print("Print List Before:\n")
    my_plist.printList()
    # Get size of linked list
    size_n = my_plist.size()

    # Check if k is less than size
    if (size_n < k):
        return (my_plist.head)

    # If x (kth node from start) and y(kth node from end) are same
    if (2 * k - 1 == size_n):
        return (my_plist.head)

    # Find the kth node from beginning of linked list. We also find
    # previous of kth node because we need to update next pointer of
    # the previous.
    x = my_plist.head
    x_prev = None
    print("iiiiiii")
    for i in range(1, k):
        print(i)
        x_prev = x
        x = x.next

    print("xval #### ", x.val)

    # Similarly, find the kth node from end and its previous. kth node
    # from end is (n-k+1)th node from beginning
    y = my_plist.head
    y_prev = None
    for i in range(1, size_n - k + 1):
        y_prev = y
        y = y.next

    # Now swap the x and y nodes
    if (x_prev):
        x_prev.next = y
    if (y_prev):
        y_prev.next = x
    save_y_next = y.next
    y.next = x.next
    x.next = save_y_next

    if k == 1:
        my_plist.head = y

    return (my_plist.head)
