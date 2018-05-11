
def num_paths():

    # dp structure
    table = [][]
    #populate

   for  i in range( len(grid)-1, 0):
        for j in range( len(grid[0])-1,0):
            if i == len(grid):
                table[i][j] = 0
            if j == len(grid[0]):
                table[i][j] = 0


