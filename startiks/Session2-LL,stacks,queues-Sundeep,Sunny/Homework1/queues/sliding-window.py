# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    def getMax(self):
        return(max(self.items))


line = "1,2,3,4,5,6,7,8"
window = 4
num_array = map(lambda x: int(x), line.split(","))
slw_q = Queue()
for i in range(0,window):
    slw_q.enqueue(num_array[i])

#find the max in the Queue
w_max = []
w_max.append(slw_q.getMax())

#repeat this till we exhaust the input array
cur_index = window
num_len = len(num_array)
while(cur_index < num_len):
    slw_q.dequeue()
    slw_q.enqueue(num_array[cur_index])
    cur_index = cur_index + 1
    w_max.append(slw_q.getMax())

print (w_max)






