def part_2():
    ranges = []

    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            if '-' in line:
                start, end = map(int, line.split('-'))
                ranges.append((start, end))

    ranges = sorted(ranges, key=lambda x: x[0])
    merged = []
    for s, e in ranges:
        if not merged or s > merged[-1][1] + 1:
            # add interval if not overlapping or first
            merged.append([s, e])
        else:
            # merge
            merged[-1][1] = max(merged[-1][1], e)

    num_fresh = 0
    for s, e in merged:
        num_fresh += (e - s + 1)

    return num_fresh

if __name__ == "__main__":
    print(part_2())
