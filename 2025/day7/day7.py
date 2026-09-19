from functools import cache

def get_diagram(filename) -> list[list]:
    diagram = []
    with open(filename, 'r') as file:
        for line in file:
            diagram.append(line)
    return diagram

def count_splits(diagram, start) -> int:
    n = len(diagram[0])
    splits = 0
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

def count_timelines(diagram, start):
    rows = len(diagram)
    cols = len(diagram[0])

    # use DP to count how many streams hit the bottom
    dp = [[0] * cols for _ in range(rows)]
    dp[0][start] = 1 # starting stream

    for r in range(rows - 1):
        for c in range(cols):
            streams = dp[r][c]
            # if no streams are running yet, just continue
            if streams == 0:
                continue

            # if here is a rock, two streams go left and right next line
            if diagram[r+1][c] == '^':
                # += streams will count properly when more than one stream passes here
                if c-1>=0:
                    dp[r+1][c-1] += streams
                if c+1<cols:
                    dp[r+1][c+1] += streams
            else:
                # no split, just continue down
                dp[r+1][c] += streams
    return sum(dp[-1]) # the numbers at the bottom are the number of streams ending at that col

def main():
    filename = 'diagram.txt'
    diagram = get_diagram(filename)
    start = diagram[0].index('S')
    split_count = count_splits(diagram, start)
    print(f'Number of splits: {split_count}')
    timeline_count = count_timelines(diagram, start)
    print(f'Number of timelines: {timeline_count}')

if __name__ == '__main__':
    main()
