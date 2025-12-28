def part_1():
    with open('input.txt') as f:
        lines = f.readlines()
        grid = [[True if c == '@' else False for c in line.strip()] for line in lines]

    num_rows, num_cols = len(grid), len(grid[0])

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

    total = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell:
                neighbour_sum = check_neighbours(grid, i, j)
                if neighbour_sum < 4:
                    # print(f"Cell at ({i}, {j}) has {neighbour_sum} neighbours.")
                    total += 1


    return total

if __name__ == "__main__":
    print(part_1())
