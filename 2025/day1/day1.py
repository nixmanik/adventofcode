file = list(open("combination.txt"))
start = 50
zeros = 0
for line in file:
    c = line.strip()
    direction = c[0]
    num = int(c[1:])
    if direction == 'R':
        to_zero = 100 - start
        if num >= to_zero:
            zeros += 1 + (num - to_zero) // 100
    else:
        to_zero = 100 if start == 0 else start
        if num >= to_zero:
            zeros += 1 + (num - to_zero) // 100
    start = (start + num) % 100 if direction == 'R' else (start - num) % 100
print(zeros)