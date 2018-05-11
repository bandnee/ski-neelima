# Complete the function below.
import sys


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def getMax(self):
        return (max(self.items))


class Cell:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

    def __str__(self):
        mystr = "(" + str(self.x) + "," + str(self.y) + ")"
        return mystr


class Grid:
    def __init__(self, grid):
        self.grid = grid
        # Get the length of the grid as rows
        self.lr = len(grid)
        # Get the length of the grid[0] as cols
        self.lc = len(grid[0])
        self.stCell = None
        self.endCell = None

    def set_start_end(self):
        # Get the length of the grid as rows
        lr = len(self.grid)
        # Get the length of the grid[0] as cols
        lc = len(self.grid[0])
        for i in range(lr):
            for j in range(lc):
                if self.stCell != None and self.endCell != None:
                    return True
                if self.grid[i][j] == "@":
                    self.stCell = Cell(i, j, "@")  # Identify the cell of @
                if self.grid[i][j] == "+":
                    self.endCell = Cell(i, j, "+")  # Identify the cell of +  as end
        # Did not find one of the start or end cells
        return False

    def isValidCell(self, x, y,visited):
        if (x < 0 or x >= self.lr or y < 0 or y >= self.lc):
            return False
        elif (self.grid[x][y] == '#'):
            return False
        elif self.grid[x][y].isalpha():
            if self.grid[x][y].isupper():
                #check if the key is found in the visited/parent list, if found
                #then return true, else :
                #Do BFS from each parent as a start and get the path count and do that for each parent
                #nd keep the min path count .
                if self.grid[x][y].lower() not in haveKeys:
                    # Do a BFS from the door to the key
                    return False
            else:
                haveKeys.add(grid[x][y])
        return True


    def isVisited(self,r,c,visited):
        this_node = Cell(r, c, self.grid[r][c])
        ###### I missed adding the visited  #########
        if (str(this_node)  in visited.keys()):
            return True
        return False


    def find_sp(self):
        if not self.set_start_end():
            return -1
        valid_rows = [1, -1, 0, 0]
        valid_cols = [0, 0, 1, -1]
        # Enqueue the first node
        # Instantiate a set to collect all the keys
        # Instantiate a dict to capture the visited and the node that it came from
        haveKeys = set([])
        visited = {}
        q = Queue()
        q.enqueue(self.stCell)
        visited[str(self.stCell)] = None
        while not q.isEmpty():
            cur_node = q.dequeue()
            print("Dequeing")
            print(cur_node)
            #print(cur_node)
            if cur_node.val == self.endCell.val:
                break
            else:
                for i in range(len(valid_rows)):
                    next_row = cur_node.x + valid_rows[i]
                    next_col = cur_node.y + valid_cols[i]
                    #print("next_row", next_row)
                    #print("next_col", next_col)
                    if self.isValidCell(next_row, next_col, haveKeys):
                        if not self.isVisited(next_row,next_col,visited):
                            this_node = Cell(next_row, next_col, self.grid[next_row][next_col])
                            visited[str(this_node)] = str(cur_node)
                            print ("Enqueing for ",str(cur_node), str(this_node))
                            q.enqueue(this_node)
                    #else:
                        #print("Not valid cell")
                        #print("End of neighbour search for ", cur_node)
        # The last cur_node is the one we are looking for
        # Now print the path
        path = []
        end = str(self.endCell)
        #print(end)
        path.append(end)
        #for key in (visited.keys()):
           # print(key)

        while visited[end] != None:
            path.append(str(visited[end]))
            end = visited[end]
        path.reverse()
        print(path)
        return(len(path))


def find_shortest_path(in_grid):
    grid = Grid(in_grid)
    return(grid.find_sp())


grid = [['.','.','.','B'],
        ['.','b','#','.'],
        ['@','#','+','.']]


grid = [['+','B','.','.','.'],
        ['#','#','#','#','.'],
        ['#','#','b','#','.'],
        ['a','.','.','.','A'],
        ['#','#','@','#','#']]

print(find_shortest_path(grid))