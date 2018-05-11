# Queue is a first-in first-out
# Process the root first, and then enqueue children

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

class Vertex:
    int data
    neighbors  = [] # array of vertices


# Traversal
def bfs (vertex):
    visited = set([vertex])
    q = Queue()
    q.enqueue(vertex)
    while not q.isEmpty():
        #process the vertex
        # and then put it's children into the Queue
        cur_v = q.dequeue()
        print(cur_v.data)
        for ng in cur_v.neighbors:
            if ng not in visited:
                #Mark it visited and deque
                visited.add(ng)
                q.dequeue(ng)


def shortest_path(st,end):
    back_refs = {st: None}
    # Enqueue in the Queue
    q.equeue(st)
    while not q.isEmpty():
        cur_v = q.dequeue
        if cur_v == end :
            break
        else:
            for ng in cur_v.neighbors:
                if ng not in back_refs:
                    back_refs{ng} = cur_v
                    q.enqueue(ng)
    if end not in back_refs.keys():
        print("There is no path")
    else:
        path = []
        cur = end
        while cur:
            path.append(cur)
            cur = back_refs{cur}
        path.reverse()
        print path
