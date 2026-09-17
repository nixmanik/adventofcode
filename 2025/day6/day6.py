import math
from itertools import zip_longest

def get_data():
    filename = 'math.txt'
    data = []
    with open(filename, 'r') as file:
        for line in file:
            thisline = [int(x) if x.isdigit() else x for x in line.split()]
            data.append(thisline)
    return data


def solve(equation):
    op = equation[-1]
    nums = equation[:-1]
    for num in range(len(equation)-1):
        if op == '+':
            return sum(equation[:-1])
        elif op == '*':
            total = math.prod(equation[:-1])
            return math.prod(equation[:-1])
    pass

# This doesn't work because they're not lined up equally
def solve_part2(equation):
    op = equation[-1]
    str_nums = []
    for num in equation[:-1]:
        str_nums.append(str(num))
    rev_str_nums = [s[::-1] for s in str_nums]
    new_nums = []
    for digits in zip_longest(*rev_str_nums, fillvalue='0'):
        new_num = int(''.join(digits))
        new_nums.append(new_num)
    new_nums.append(op)
    total = solve(new_nums)

    return total






def main():
    data = get_data()
    equations = list(zip(*data))
    total = 0
    for e in equations:
        total += solve(e)
    print(total)
    total = 0
    for e in equations:
        total += solve_part2(e)

if __name__ == "__main__":
    main()
