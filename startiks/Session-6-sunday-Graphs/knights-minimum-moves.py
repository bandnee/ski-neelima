# First create a  cell datastructure that
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

class Cell:

    def __init__(self,row,col,dist):
        self.x = row
        self.y = col
        self.dist = dist

class knightChess:
    def __init__(self,rows,cols):
        self.bd_rows =  rows
        self.bd_cols = cols

    #Function to check if it is a valid cell:
    def _isValidCell(self,x y):
        if x < 0 || x == self.bd_rows || y < 0 || y == self.bd_cols:
            return False
        return True

    def shortestPath(st,end) :

        #First Form the array of moves that the knight needs to move in col /row at the same time
        row_moves = {2,2,-2,-2,1,1,-1,-1}
        col_moves = {1,-1,1,-1,2,-2,2,-2}

        q = Queue()
        #Enqueue the first element with the st co-ordinates
        visited = {}
        visited{st} = None
        q.enqueue(st)
        cur_cell = None
        while not q.isEmpty():
            #dequeue the element and check if the node is the one we are looking for,
            # if so return it
            cur_cell = q.dequeue()
            if cur_cell.x == end.x and cur_cell.y == end.y:
                break
            else :
                for i in range(len(row_moves)):
                    childCell = Cell(cur_cell.x + row_moves[i],
                                     cur_cell.y + col_moves[i],
                                     cur_cell.dist + 1)
                    if self._isValidCell(childCell.x,childCell.y):
                        #if it is not visited , enqueue into hash
                        if childCell not  in visited.keys :
                            visited{childCell} = cur_cell
                            q.enqueue(childCell)

        # Print the Path itself :
        dist = cur_cell.dist
        path = []
        str = join(cur_cell.x  . " +" .cur_cell.y)
        path.append(str)
        while visited{cur_cell} :
            cur_cell = visited{cur_cell}
            a = "+"
            str = a.join(cur_cell.x,cur_cell.y)
            path.append(str)


__main__
start = Cell(1,2,0)
end = Cell(4,3,0)

kc = knightChess(5,5)
(path_size, path) = kc.shortestPath(start,end)


