def part_1():
    with open("input.txt") as f:
        l = f.readline().strip()

    
    ranges = l.split(",")
    ranges = [tuple(map(int, r.split("-"))) for r in ranges]

    total = 0
    for r in ranges:
        start, end = r

        # start and end based on repeating digit limits
        start = 10 ** len(str(start)) if len(str(start)) % 2 == 1 else start
        end = 10 ** (len(str(end)) - 1) - 1 if len(str(end)) % 2 == 1 else end

        start = str(start)
        end = str(end)

        if start > end:
            continue

        # generate numbers in the range
        start_left = start[:len(start) // 2]
        end_left = end[:len(end) // 2]

        # generate all matching numbers
        for i in range(int(start_left), int(end_left) + 1):
            candidate = int(str(i) + str(i))
            if int(start) <= candidate <= int(end):
                total += candidate
        

    return total


if __name__ == "__main__":
    print(part_1())
