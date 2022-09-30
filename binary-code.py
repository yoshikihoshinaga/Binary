# Name: Yoshiki Hoshinaga
# Date: 8/10/2020

import random

def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []
    
    for r in range(height):
        row = [0] * width     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line, and nothing between values.
        input: grid is a 2-D list. We assume that all of the cell
        values are integers between 0 and 9.
    """
    height = len(grid)
    width = len(grid[0])
    
    for r in range(height):
        for c in range(width):
            print(grid[r][c], end='')   # print nothing between values
        print()                         # at end of row, go to next line

def create_new_grid(height,width):
    """creates and returns a new 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    new_grid=[]

    for r in range(height):
        row = [0] * width  # a row containing width 0s
        new_grid += [row]
    return new_grid

def print_new_grid(grid):
     """ prints new 2-D list specified by grid in 2-D form,
        with each row on its own line, and nothing between values.
        input: grid is a 2-D list. We assume that all of the cell
        values are integers between 0 and 9.
    """
     height = len(new_grid)
     width = len(new_grid[0])

     for r in range(height):
          for c in range(width):
               print(grid[r][c],end='')    #print nothing between values 
          print()                         # at end of row, go to next line

#0
def diagonal_grid(height, width):
    """ creates and returns a height x width grid in which the cells
        on the diagonal are set to 1, and all other cells are 0.
        inputs: height and width are non-negative integers
    """
    grid = create_grid(height, width)   # initially all 0s

    for r in range(height):
        for c in range(width):
            if r == c:
                grid[r][c] = 1

    return grid
#1
def inner_grid(height,width):
    """ creates and returns a height x width grid in which the cells
        on the diagonal are set to 1, and all other cells are 0.
        inputs: height and width are non-negative integers
    """
    grid = create_grid(height,width)
    for r in range(1,height-1):
        for c in range(1,width-1):
                grid[r][c]=1
    return grid
#2
def random_grid(height, width):
    """creates and returns a 2-D list of height rows and width columns
        in which the inner cells are randomly assigned either 0 or 1,
        but the cells on the outer border are all 0
    """
    grid = create_grid(height, width)
    for r in range(1, height - 1):
        for c in range(1, width - 1):
                grid[r][c] = random.choice([0, 1])
    return grid
#3
def copy(grid):
    """creates and returns a deep copy of grid, a new, separate 2-D list
        that has the same dimensions and cell values as grid
    """
    new_grid = []
    height = len(grid)
    width = len(grid[0])
    new_grid = create_new_grid(height, width)
    for r in range(height):
        for c in range(width):
            new_grid[r][c] = grid[r][c]
    return new_grid
#4
def invert(grid):
    """ takes an existing 2-D list of 0s and 1s and inverts it – changing all 0 values to 1, and changing all 1 values to 0."""
    #height for rows
    height=len(grid)
    #width for columns
    width=len(grid[0])
    for r in range(height):
        for c in range(width):
            if grid[r][c]==1:
                grid[r][c]=0
            else:
                grid[r][c]=1


    

if __name__=='__main__':
    #0
    grid0=diagonal_grid(6,8)
    print_grid(grid0)
    print('')
    #1
    grid1 = inner_grid(5, 5)
    print_grid(grid1)
    print('')
    #""
    grid2 = random_grid(10, 10)
    print_grid(grid2)
    print('')
    #3
    grid1 = create_grid(2, 2)
    grid2 = grid1      # copy grid1 into grid2
    print_grid(grid2)
    print('')
    grid1[0][0] = 1
    print_grid(grid1)
    print('')
    print_grid(grid2)
    print('')
    grid1 = diagonal_grid(3, 3)
    print_grid(grid1)
    print('')
    grid2 = copy(grid1)   # should get a deep copy of grid1
    print_grid(grid2)
    print('')
    grid1[0][1] = 1
    print_grid(grid1)     # should see an extra 1 at [0][1]
    print('')
    print_grid(grid2)     # should not see an extra 1
    print('')
    #4
    grid00 = diagonal_grid(5, 5)
    print_grid(grid00)
    print('')
    invert(grid00)
    print_grid(grid00)
    print('')
    grid1 = inner_grid(5, 5)
    print_grid(grid1)
    print('')
    grid2 = grid1
    grid3 = grid1[:]
    invert(grid1)
    print_grid(grid1)
    print('')
