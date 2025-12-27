def part_2():
    with open("input.txt") as f:
        l = f.readline().strip()

    
    ranges = l.split(",")
    ranges = [tuple(map(int, r.split("-"))) for r in ranges]

    total = 0

    for r in ranges:
        start, end = r
        candidates = set()

        def ceil_div(a, b):
            return (a + b - 1) // b

        min_len = len(str(start))
        max_len = len(str(end))

        for total_len in range(min_len, max_len + 1):
            low = max(start, 10 ** (total_len - 1))
            high = min(end, 10 ** total_len - 1)
            if low > high:
                continue

            for base_len in range(1, total_len // 2 + 1):
                if total_len % base_len != 0:
                    continue
                repeats = total_len // base_len
                if repeats < 2:
                    continue

                pow10_base = 10 ** base_len
                # Multiplier for repeating the base block 'repeats' times.
                multiplier = (10 ** (base_len * repeats) - 1) // (pow10_base - 1)

                base_min = max(10 ** (base_len - 1), ceil_div(low, multiplier))
                base_max = min(10 ** base_len - 1, high // multiplier)
                if base_min > base_max:
                    continue

                for base in range(base_min, base_max + 1):
                    candidates.add(base * multiplier)

        total += sum(candidates)
    return total

if __name__ == "__main__":
    print(part_2())
