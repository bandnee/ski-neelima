from BinHeap import BinaryHeap
import sys

m_lists = [ [1,2,3,4,11,22,33,44], [5,6,7,8,23,34,45,55], [7,8,9,10,13,24,35,46]]

k=len(m_lists)
n_size = len(m_lists[0])

# Go over each array:

#Make a BinHeap
bin_heap = BinaryHeap()
# value, array,index_of_next_element
bin_heap.insert([m_lists[0][0], 0, 1])
bin_heap.insert([m_lists[1][0], 1, 1])
bin_heap.insert([m_lists[2][0], 2, 1])
bin_heap.printHeap()

# If the sizes are varied , add all the sizes instead of the multiple
# Implement with python
# Time complexity is nlogk
res_array = []
for i in range(k*n_size):
    next_tuple = bin_heap.getMin()
    bin_heap.delMin()
    res_array.append(next_tuple[0])
    next_array =  next_tuple[1]
    next_index = next_tuple[2]
    # If the sizes are varied , check this against each sized arrays
    if(next_index < n_size) :
        bin_heap.insert([m_lists[next_array][next_index],next_array,next_index+1])


































