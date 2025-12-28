def part_1():
    ranges = []
    ids = []
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            if '-' in line:
                start, end = map(int, line.split('-'))
                ranges.append((start, end))
            elif line.isdigit():
                ids.append(int(line))

    ranges = sorted(ranges, key=lambda x: x[0])
    merged = []
    for s, e in ranges:
        if not merged or s > merged[-1][1] + 1:
            # add interval if not overlapping or first
            merged.append([s, e])
        else:
            # merge
            merged[-1][1] = max(merged[-1][1], e)


    def search_ranges(search_id):
        """binary search"""
        start, end = 0, len(merged) - 1
        while start <= end:
            mid = (start + end) // 2
            if merged[mid][0] <= search_id <= merged[mid][1]:
                return True
            elif search_id > merged[mid][1]:
                start = mid + 1
            else:
                end = mid - 1

        return False    
        
    num_fresh = 0
    for search_id in ids:
        if search_ranges(search_id):
            num_fresh += 1

    return num_fresh

if __name__ == "__main__":
    print(part_1())
