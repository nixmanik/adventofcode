import math

def get_data():
    filename = 'day6.txt'
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line)
    # print(data)
    return data 

def get_equations(data):
    equations = []
    op = None
    e = []
    for i, col in enumerate(zip(*data)):
        num = []
        for ch in col:
            if ch.isdigit():
                num.append(ch)
            elif ch == '+' or ch == '*':
                op = ch
        if ''.join(num).isdigit():
            e.append(int(''.join(num)))
        elif op:
            e.append(op)
            equations.append(e)
            e = []

    return equations

def solve(equation):
    op = equation[-1]
    if op == '+':
        return (sum(equation[:-1]))
    return math.prod(equation[:-1])

def main():
    hw = get_data()
    equations = get_equations(hw)
    print(equations[0])
    total = 0
    for e in equations:
        adding = solve(e)
        total += adding
        print(f'Total: {total} added {adding}')

if __name__ == '__main__':
    main()
