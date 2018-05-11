from BinHeap import BinaryHeap
import sys

in_list = [1,2,3,4,11,22,33,44,5,6,7,8,23,34,45,55,7,8,9,10,13,24,35,46]
k=5

#Make a BinHeap
bin_heap = BinaryHeap()
for i in range(k):
    # build a min-heap
    bin_heap.insert([in_list[i]])

bin_heap.printHeap()

for j in range(k,len(in_list)):
    min  = bin_heap.getMin()
    if in_list[j] > min[0]:
        #insert the element without heapifyUp
        #delete the min , which will do heapifyDown
        bin_heap.insert_without_hup([in_list[j]])
        bin_heap.delMin()
   # bin_heap.printHeap()

bin_heap.printHeap()
