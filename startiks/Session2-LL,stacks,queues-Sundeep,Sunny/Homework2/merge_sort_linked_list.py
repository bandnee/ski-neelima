import sys
import os


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


def mergeSortList(pList):
    my_plist = LinkedList()
    while (pList):
        my_plist.insert_at_tail(pList.val)
        pList = pList.next
    return (my_mergeSortList(my_plist).head)


def my_mergeSortList(plist):
    if plist.head == None or plist.head.next == None:
        return plist
    llist = LinkedList()
    rlist = LinkedList()
    mergeSortSplit(plist, llist, rlist)
    '''pllist = llist
    prlist = rlist
    itr = 0
    while (pllist):
        print ("Itr ", itr)
        print(pllist.val)
        pllist= pllist.next
        itr = itr + 1
    itrr = 10 
    while (prlist):
        print ("Itr ", itrr)
        print(prlist.val)
        prlist= prlist.next
        itrr = itrr + 1
    '''
    llist = my_mergeSortList(llist)
    rlist = my_mergeSortList(rlist)
    return (merge(llist, rlist))


def mergeSortSplit(pList, llist, rlist):
    s_ptr = pList.head
    llist.head = s_ptr
    f_ptr = pList.head
    while (f_ptr.next != None and f_ptr.next.next != None):
        s_ptr = s_ptr.next
        f_ptr = f_ptr.next.next
    rlist.head = s_ptr.next
    s_ptr.next = None
    s_ptr.next = None


def merge(llist: LinkedList, rlist: LinkedList):
    fll = LinkedList()
    fll_ptr = fll.head
    llist_ptr = llist.head
    rlist_ptr = rlist.head
    while (llist_ptr != None and rlist_ptr != None):
        if llist_ptr.val <= rlist_ptr.val:
            fll.insert_at_tail(llist_ptr.val)
            llist_ptr = llist_ptr.next
        else:
            fll.insert_at_tail(rlist_ptr.val)
            rlist_ptr = rlist_ptr.next
    while (llist_ptr != None):
        fll.insert_at_tail(llist_ptr.val)
        llist_ptr = llist_ptr.next
    while (rlist_ptr != None):
        fll.insert_at_tail(rlist_ptr.val)
        rlist_ptr = rlist_ptr.next
    return fll


def merge_inplace(llist: LinkedList, rlist: LinkedList):

    newlist_head = None
    llist_ptr = llist.head
    rlist_ptr = rlist.head

    if (llist_ptr != None and rlist_ptr != None):
        if llist_ptr.val <= rlist_ptr.val:
            newlist_head = llist_ptr
            llist_ptr = llist_ptr.next
        else:
            newlist_head = rlist_ptr
            rlist_ptr = rlist_ptr.next
    elif (llist_ptr == None && rlist_ptr != None):
        newlist_head = rlist_ptr
        rlist_ptr = rlist_ptr.next
    else (llist_ptr != None && rlist_ptr == None):
        newlist_head = llist_ptr
        llist_ptr = llist_ptr.next

    newlist_prev = newlist_head
    while(llist_ptr != None and rlist_ptr != None):
        if llist_ptr.val <= rlist_ptr.val:
            newlist_prev.next = llist_ptr
            newlist_prev = newlist_prev.next
            llist_ptr = llist_ptr.next
        else:
            newlist_prev.next = rlist_ptr
            newlist_prev = newlist_prev.next
            rlist_ptr = rlist_ptr.next

    while (llist_ptr != None):
        newlist_prev.next = llist_ptr
        newlist_prev = newlist_prev.next
        llist_ptr = llist_ptr.next
    while (rlist_ptr != None):
        newlist_prev.next = rlist_ptr
        newlist_prev = newlist_prev.next
        rlist_ptr = rlist_ptr.next

    return newlist_head


