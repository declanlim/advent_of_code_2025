def part_1():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    pos = 50
    zero_count = 0

    for l in lines:
        direction = l[0]
        distance = int(l[1:])

        if direction == "R":
            pos += distance
        elif direction == "L":
            pos -= distance

        if pos % 100 == 0:
            zero_count += 1

    return zero_count


if __name__ == "__main__":
    print(part_1())
