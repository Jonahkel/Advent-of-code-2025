def main():
    with open("day-04.txt", 'r') as file:
        grid = []
        for line in file:
            grid.append(list(line.strip()))

        num_reachable = -1
        new_reachable = 0
        new_grid = grid.copy()
        while new_reachable != num_reachable:
            num_reachable = new_reachable
            for row, row_list in enumerate(grid):
                for col, char in enumerate(row_list):
                    if char != '@': continue
                    #Start with top, then go around in a circle
                    surrounding = 0
                    if row != 0 and grid[row-1][col] == '@':
                        surrounding+=1
                    if row!= 0 and col != len(row_list) -1 and grid[row-1][col+1] == '@':
                        surrounding+=1
                    if col != len(row_list) -1  and grid[row][col+1] == '@':
                        surrounding+=1
                    if row != len(grid) -1 and col != len(row_list) -1 and grid[row+1][col+1] == '@':
                        surrounding+=1
                    if row != len(grid) -1 and grid[row+1][col] == '@':
                        surrounding+=1
                    if row != len(grid) -1 and col != 0 and grid[row+1][col-1] == '@':
                        surrounding+=1
                    if col != 0 and grid[row][col-1] == '@':
                        surrounding+=1
                    if row != 0 and col != 0 and grid[row-1][col-1] == '@':
                        surrounding+=1

                    if surrounding < 4:
                        new_reachable+=1
                        new_grid[row][col] = '.'

            grid = new_grid
            new_grid = grid.copy()
                
        print(num_reachable)
                
                

if __name__ == "__main__":
    main()