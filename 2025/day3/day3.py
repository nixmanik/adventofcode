banks = []
with open('voltages.txt', 'r') as file:
    banks = file.read().splitlines()

total = 0
n = len(banks[0])
for bank in banks:
    best_digit = float('-inf')
    best_twodigit = float('-inf')
    for char in reversed(bank):
        digit = int(char)

        if best_digit != float('inf'):
            current = digit * 10 + best_digit
            best_twodigit = max(current, best_twodigit)

        
        best_digit = max(best_digit, digit)
    total += best_twodigit

print(total)

total = []

banksize = 15
wsize = 12
biggest_first = 0
first_i = 0
for bank in banks:
    for ch in range(banksize - wsize, wsize+1):
        num = int(ch)
        if num > biggest_first:
            biggest_first = bank[ch]
            first_i = ch

def twelve_batts(bank) -> int:
    removes = len(bank)-12
    stack = []
    for batt in bank:
        while removes > 0 and stack and stack[-1] < digit:
            stack.pop()
            removes -= 1
        stack.append(digit)
    if removes > 0:
        stack = stack[:-removes]

    return int(''.join(stack))