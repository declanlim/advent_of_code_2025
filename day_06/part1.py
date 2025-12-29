from functools import reduce

def part_1():
    with open('input.txt') as f:
        problems = []
        lines = f.readlines()
        for line in lines[:-1]:
            line = line.strip()
            problems.append(list(map(int, line.split())))

        problems.append(list(lines[-1].strip().split()))


    num_prob = len(problems[0])

    def add(a,b):
        return a + b
    
    def mul(a,b):
        return a * b

    total = 0
    for i in range(num_prob):
        tmp = [problems[j][i] for j in range(len(problems))]
        operands = tmp[:-1]
        operator = tmp[-1]
        if operator == '+':
            func = add
        elif operator == '*':
            func = mul

        result = reduce(func, operands)
        total += result

    return total

    

if __name__ == "__main__":
    print(part_1())
