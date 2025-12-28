def part_2():
    with open("input.txt") as f:
        lines = f.readlines()

    total = 0 

    def get_largest(substring):
        """get the largest digit and return it and its index"""
        max_digit = max(substring)
        max_index = substring.find(max_digit)

        return max_digit, max_index

    for line in lines:
        line = line.strip()
        substr_start = 0
        bank_joltage = ""
        for rem in range(12):
            remaining = rem - 11
            if remaining == 0:
                remaining = None
            
            substring = line[substr_start:remaining]
            max_digit, max_index = get_largest(substring)
            substr_start += max_index + 1
            bank_joltage += max_digit
        
        total += int(bank_joltage)

    return total


if __name__ == "__main__":
    print(part_2())
