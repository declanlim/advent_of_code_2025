def part_2():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    pos = 50
    zero_count = 0

    for l in lines:
        direction = l[0]
        distance = int(l[1:])

        old_pos = pos

        if direction == "R":
            pos += distance
            zero_count += pos // 100 - old_pos // 100
        elif direction == "L":
            pos -= distance
            zero_count += (old_pos - 1) // 100 - (pos - 1) // 100

    return zero_count


if __name__ == "__main__":
    print(part_2())