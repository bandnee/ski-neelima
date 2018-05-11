# Enter your code here. Read input from STDIN. Print output to STDOUT

# Complete the function below.

#For your reference:
#LinkedListNode {
#    int val
#    LinkedListNode next
#}

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
        print("Size:", count )
        return count



def reverseNodes(k):
    my_plist = LinkedList()
    my_array = [1,2,3,4,5,6,7,8]
    for num in  (my_array):
    #while(pList):
        my_plist.insert_at_tail(num)
        #my_plist.insert_at_tail(pList.val)
        #pList = pList.next
    print("Print List Before:\n")
    my_plist.printList()
    #Get size of linked list
    size_n = my_plist.size()
    current = my_plist.head
    fll  = LinkedList()
    interim_ll = LinkedList()
    start_r =1
    end_r = k
    while(current):
        for i in range(start_r,end_r+1):
            if(current):
                interim_ll.insert_at_head(current.val)
                current = current.next
        start_r = end_r + 1
        end_r = end_r + k
        interim_ll.printList()
        if (fll.head == None) :
            fll.head = interim_ll.head
        else :
            fll.tail.next = interim_ll.head
        interim_ll.head = LinkedList()
    fll.printList()
    return(fll.head)



#_constantMem
def reverse_linked_list_in_groups_of_k(my_plist,k):
    current = my_plist
    fll_head = None
    start_r =1
    end_r = k
    prev = None
    fll_tail = None
    while(current):
        for i in range(start_r,end_r+1):
            if(current):
                if prev == None :
                    prev_tail = current
                next_e = current.next
                current.next = prev
                prev = current
                current = next_e
        start_r = end_r + 1
        end_r = end_r + k
        #Mistake , set it to current
        if (fll_head == None) :
            fll_head = prev
        else :
            fll_tail.next = prev
            fll_tail = None
        #first set, prev tail's current-head and remember next_tail
        if(fll_tail == None):
            fll_tail = prev_tail
        prev = None
    return(fll_head)


def reverseNodes_constantMem(k):
    my_plist = LinkedList()
    my_array = [1,2,3,4,5,6,7,8]
    for num in  (my_array):
        my_plist.insert_at_tail(num)
    print("Print List Before:\n")
    my_plist.printList()
    #Get size of linked list
    size_n = my_plist.size()
    current = my_plist.head
    fll  = LinkedList()
    interim_ll = LinkedList()
    start_r =1
    end_r = k
    prev = None
    fll_tail = None
    while(current):
        for i in range(start_r,end_r+1):
            if(current):
                if prev == None :
                    fll_tail = current
                next = current.next
                current.next = prev
                prev = current
                current = next
        start_r = end_r + 1
        end_r = end_r + k
        if (fll_head == None) :
            fll_head = prev
        else :
            fll_tail.next = prev
        prev = None
    return(fll_head)


reverseNodes(3)