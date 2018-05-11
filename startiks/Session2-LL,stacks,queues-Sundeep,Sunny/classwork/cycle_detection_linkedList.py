#!/bin/python3

import sys
import os

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None

class LinkedList:


    # Function to initialize head
    def __init__(self):
        self.head = None
        self.meetpoint = None


    def detect_loop(self):
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p  and fast_p.next) :
            if (slow_p == fast_p) :
                self.meetpoint = slow_p
                return True
            else :
                slow_p = slow_p.next
                fast_p = fast_p.next.next
        return False

    #start a pointer from meetpoint
    #once the pointer reaches the meetpoint that is the length of the loop
    def count_loop_length (self):
        count_p = self.meetpoint
        count =0
        while (count_p.next != self.meetpoint):
            count = count + 1
            count_p = count_p.next
        return count


    # start the pointer from head and a pointer  from meetpoint
    #when they meet that is the  start of the loop based on
    # m + k = n( Cf - 2 * Cs)
    #Where m is the nodes travelled from head to beginning of loop
    # k is nodes from beg of loop to meetpoint
    # n length of loop
    #Cf is no of cycles for fast pointer
    #Cs is the no of cycles for slow pointer
    def get_loop_startnode(self):
        start_p = self.head
        meet_p = self.meetpointer
        while (meetp_p != start_p):
            start_p = start_p.next
            meet_p = meet_p.next
        return meet_p

