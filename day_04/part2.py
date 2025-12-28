def part_2():
    with open('input.txt') as f:
        lines = f.readlines()
        grid = [[True if c == '@' else False for c in line.strip()] for line in lines]

    num_rows, num_cols = len(grid), len(grid[0])
    neighbour_counts = {i: {j: 0 for j in range(num_cols)} for i in range(num_rows)}
    remove_list = []

    def check_neighbours(grid, i, j):
        neighbour_sum = 0
        neighbours = [(-1,-1), (-1,0), (-1,1),
                      (0,-1), (0,1),
                      (1,-1),  (1,0), (1,1)]
        
        for di, dj in neighbours:
            ni, nj = i + di, j + dj
            if not((0 <= ni < num_rows) and (0 <= nj < num_cols)):
                continue
            
            neighbour_sum += grid[ni][nj]

        return neighbour_sum
    
    def update_neighbours(neighbour_counts, i, j):
        """update neigbour counts and return new cells with < 4 rolls of paper"""
        neighbours = [(-1,-1), (-1,0), (-1,1),
                (0,-1), (0,1),
                (1,-1),  (1,0), (1,1)]
        
        new_free = []

        for di, dj in neighbours:
            ni, nj = i + di, j + dj
            if not((0 <= ni < num_rows) and (0 <= nj < num_cols)):
                continue
            neighbour_counts[ni][nj] = max(0, neighbour_counts[ni][nj] - 1)
            if neighbour_counts[ni][nj] == 3:
                new_free.append((ni, nj))

        return new_free


    total_removed = 0
    # populate neighbour counts and initial remove list
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell:
                neighbour_sum = check_neighbours(grid, i, j)
                neighbour_counts[i][j] = neighbour_sum
                if neighbour_sum < 4:
                    remove_list.append((i,j))

    while len(remove_list) > 0:
        i, j = remove_list.pop(0)
        total_removed += 1
        new_free = update_neighbours(neighbour_counts, i, j)

        if len(new_free) > 0:
            remove_list.extend(new_free)


    return total_removed


if __name__ == "__main__":
    print(part_2())
