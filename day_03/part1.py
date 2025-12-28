def part_1():
    with open("input.txt") as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        line = line.strip()
        for start in range(9,0,-1):
            start_idx = line[:-1].find(str(start))
            if start_idx != -1:
                break

        total += int(line[start_idx] + (max(line[start_idx +1:])))
    return total



if __name__ == "__main__":
    print(part_1())
