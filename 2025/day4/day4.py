def get_rolls():
    with open('rolls.txt', 'r') as file:
        return [list(line) for line in file.read().splitlines()]

def under_four_rolls(rolls, y, x):
    if rolls[y][x] != "@":
        return False

    rollcount = 0
    surrounds = [(-1, 0), (-1,-1), (-1,1), (1,0), (1,-1), (1,1), (0,1), (0,-1)]

    for dy, dx in surrounds:
        thisy = y + dy
        thisx = x + dx
        if not (0 <= thisy < len(rolls)): continue
        if not (0 <= thisx < len(rolls[thisy])): continue

        if rolls[thisy][thisx] == "@":
            rollcount += 1 

    return rollcount < 4

def get_accessible(rolls):
    accessible = []
    for r, row in enumerate(rolls):
        for c, cell in enumerate(row):
            if under_four_rolls(rolls, r, c):
                accessible.append((r,c))
    return accessible

def del_accessible(rolls):
    removed = 0
    while True:
        accessible = get_accessible(rolls)
        if not accessible: break

        removed += len(accessible)
        
        for r,c in accessible:
            rolls[r][c] = '.'
    return removed

def main():
    rolls = get_rolls()
    accessible = get_accessible(rolls)
    print(f'Part 1: {len(accessible)} rolls')
    removed = del_accessible(rolls)
    print(f'Part 2: Removed {removed} rolls')

if __name__ == "__main__":
    main()