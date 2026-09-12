banks = []
with open('voltages.txt', 'r') as file:
    banks = file.read().splitlines()

total = 0

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