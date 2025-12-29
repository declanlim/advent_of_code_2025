from functools import reduce

def part_2():
    with open('input.txt') as f:
        problems = []
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            problems.append(list(line))

    def add(a,b):
        return a + b
    
    def mul(a,b):
        return a * b


    # adjust final value in each row
    for p in problems:
        p = p.append(' ')

    total = 0
    num_chars = len(problems[0])
    start_col = [0]

    for i in range(num_chars):
        if problems[0][i] == problems[1][i] == problems[2][i] == problems[3][i] == ' ':
            start_col.append(i + 1)


    for i in range(1, len(start_col)):
        col_start = start_col[i - 1]
        col_end = start_col[i]


        num_digits = col_end - col_start - 1

        numbers = []
        for j in range(num_digits):
            # read numbers from column
            numbers.append(int("".join([problems[k][col_start + j] for k in range(4)])))

        operator = problems[4][col_start:col_end]

        if '+' in operator:
            func = add
        elif '*' in operator:
            func = mul

        result = reduce(func, numbers)
        total += result
        

    return total


if __name__ == "__main__":
    print(part_2())
