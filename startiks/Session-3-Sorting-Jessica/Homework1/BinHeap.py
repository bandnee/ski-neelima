class BinaryHeap():

    def __init__(self):
        self.heapList = [[0,0,0]]
        self.currentSize = 0
        # For a parent p
        # Left Child is 2p
        # Right Child is 2p+1

    def size(self):
        return(self.currentSize)
    def getMin(self):
        return self.heapList[1]

    def printHeap(self):
        print(self.heapList)

    # log K
    def delMin(self):
        # swap the last element with the root and get rid of the last element
        self.heapList[1], self.heapList[self.currentSize] = self.heapList[self.currentSize] , self.heapList[1]
        self.heapList.pop()
        #print(self.heapList[1])
        self.currentSize = self.currentSize - 1
        self.heapifyDown()
        #print("After heapify Down")
        #self.printHeap()

    #used only of kth small elements
    def insert_without_hup(self,item):
        # append the new element and don't heapifyUp
        self.heapList.append(item)
        self.currentSize = self.currentSize + 1

    #log K
    def insert(self, item):
            # append the new element and heapifyUp
            self.heapList.append(item)
            self.currentSize = self.currentSize + 1
            self.heapifyUp()


    def heapifyUp(self):
        # first get the size of current_list
        # Get the previous parent of item to heapified up
        p_index = self.currentSize // 2
        heapify_elem_index = self.currentSize
        while (p_index > 0 and (self.heapList[p_index][0] > self.heapList[heapify_elem_index][0])):
            tmp = self.heapList[p_index]
            self.heapList[p_index] = self.heapList[heapify_elem_index]
            self.heapList[heapify_elem_index] = tmp
            heapify_elem_index = p_index
            p_index = p_index // 2

    def heapifyDown(self):
        h_index = 1
        cl_index = (2 * h_index)
        cr_index = (2 * h_index) + 1
        while ((cl_index <= self.currentSize)):
            #print (cr_index, cl_index,self.currentSize )
            if( cr_index > self.currentSize or (self.heapList[cl_index][0] < self.heapList[cr_index][0])):
                min_child  = cl_index
            else:
                min_child = cr_index
            if (self.heapList[h_index][0] > self.heapList[min_child][0]):
                tmp = self.heapList[h_index]
                self.heapList[h_index] = self.heapList[min_child]
                self.heapList[min_child] = tmp
                h_index = min_child
                #self.heapList[h_index], self.heapList[cl_index] = self.heapList[cl_index],self.heapList[h_index]
            else:
                break
            cl_index = (2 * h_index)
            cr_index = (2 * h_index) + 1
        return








