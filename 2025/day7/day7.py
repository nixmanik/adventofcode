from functools import cache

def get_diagram(filename) -> list[list]:
    diagram = []
    with open(filename, 'r') as file:
        for line in file:
            diagram.append(line)
    return diagram

def count_splits(diagram) -> int:
    n = len(diagram[0])
    splits = 0
    start = diagram[0].index('S')
    beams = [start]
    for i, line in enumerate(diagram[1:]):
        newbeams = []
        for j, spot in enumerate(line):
            if spot == '^' and j in beams:
                split_l, split_r = j-1, j+1
                newbeams.extend([split_l, split_r])
                splits += 1
            elif j in beams:
                newbeams.append(j)
        beams = newbeams
    return splits


def main():
    filename = 'diagram.txt'
    diagram = get_diagram(filename)
    split_count = count_splits(diagram)
    print(f'Number of splits: {split_count}')
if __name__ == '__main__':
    main()