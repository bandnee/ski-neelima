class Node :
    def __init__(self,val):
        self.next = None
        self.val = val


    def printList(self,Node):
        while (Node):
            print("val" , Node.val)
            if Node.next :
                print("node_next_val", Node.next.val)
            Node = Node.next

    def getNode(self,node,num):
        while(node):
            if node.val == num :
                return node
            else:
                node = node.next


def add_2_nos_ll(l1,l2):
    head = None
    prev_node = None
    carry = 0
    while l1 != None and l2 != None :
        this_sum = (l1.val + l2.val + carry) % 10
        carry =  (l1.val + l2.val + carry) // 10
        #instantiate a new node
        this_node = Node(this_sum)
        if head == None:
            head = this_node
        else:
            prev_node.next = this_node
        prev_node = this_node
        l1 = l1.next
        l2 =l2.next

    while(l1):
        this_sum = (l1.val + carry) % 10 +
        carry = (l1.val + carry) // 10
        this_node = Node(this_sum)
        prev_node.next = this_node
        prev_node = this_node
        l1 = l1.next
    while (l2):
        this_sum = (l2.val + carry) % 10 +
        carry = (l2.val + carry) // 10
        this_node = Node(this_sum)
        prev_node.next = this_node
        prev_node = this_node
        l2=l2.next

    if carry:
        prev_node.next = Node(carry)

    return head


