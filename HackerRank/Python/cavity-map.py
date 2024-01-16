try:
    from raw_input import input
except ImportError:
    pass


def cavityMap(grid):
    for i in range(1,(len(grid)-2)+1):
        for j in range(1,(len(grid)-2)+1):
            if grid[i][j]>max(grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]):
                grid[i][j]='X'
    for i in range(len(grid)):
        print (''.join(grid[i]))


if __name__ == '__main__':
    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append([x for x in grid_item])

    cavityMap(grid)
