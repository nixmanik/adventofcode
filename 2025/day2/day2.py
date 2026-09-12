with open("puzzle.txt", 'r') as file:
    content = file.read()

puzzle = [item.strip() for item in content.split(',')]
count = 0
id_numbers = []
for p in puzzle:
    first, last = p.split('-')
    id_range = list(range(int(first),int(last)))
    id_numbers.extend(id_range)

for num in id_numbers:
    s_id = str(num)
    if len(s_id) % 2 != 0:
            continue
    mid = len(s_id) // 2

    if s_id[:mid] == s_id[mid:]:
        count += num


print(count)


# part two

# count = 0

count = 0

for num in id_numbers:
    s_id = str(num)
    n = len(s_id)
    
    # Check possible repeating pattern lengths from 1 up to half the string length
    for l in range(1, n // 2 + 1):
        # A pattern can only repeat perfectly if its length divides the total length
        if n % l == 0:
            pattern = s_id[:l]
            # Check if multiplying the pattern reconstructs the full ID
            if pattern * (n // l) == s_id:
                count += num
                break  # Stop checking smaller patterns once a match is found

print(count)