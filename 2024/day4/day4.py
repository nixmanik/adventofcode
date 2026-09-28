from pathlib import Path

class WordSearch:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.directions = [
                (0,1),(0,-1),(1,0),(-1,0),
                (1,1),(-1,-1),(-1,1),(1,-1)
        ]
        with open(filename, 'r') as file:
            self.data = [list(line.strip()) for line in file]

    def print_wordsearch(self):
        for line in self.data:
            print(line)

    def is_match(self, row, col, n, dr, dc):
        return 0 <= row < len(self.data) and \
               0 <= col < len(self.data[0]) and \
               0 <= row + dr * (n-1) < len(self.data) and \
               0 <= col + dc * (n-1) < len(self.data[0])

    def _check_direction(self, row, col, word, dr, dc):
        n = len(word)
        if not self.is_match(row, col, n, dr, dc):
            return False
        for i in range(n):
            if self.data[row + dr * i][col + dc * i] != word[i]:
                return False
        return True

    def find(self, word):
        n = len(word)
        print(f'Finding {word}...')
        total = 0
        for row, line in enumerate(self.data):
            for col, ch in enumerate(line):
                if self.data[row][col] == word[0]:
                    for dr, dc in self.directions:
                        if self._check_direction(row, col, word, dr, dc):
                            total += 1
        print(f'Total found = {total}')


    def x_find(self, word):
        print(f'Finding X\'s of {word}...')
        total = 0
        n = len(word)
        cross = word[n//2]
        rev = word[::-1]

        def check_axis(dirs):
            return any(
                self._check_direction(row - dr * (n // 2), col - dc * (n // 2), word, dr, dc) or
                self._check_direction(row - dr * (n // 2), col - dc * (n // 2), rev, dr, dc)
                for dr, dc in dirs
            )

        axis1_dirs = [(-1, -1), (1, 1)]
        axis2_dirs = [(-1, 1), (1, -1)]

        for row, line in enumerate(self.data):
            for col, ch in enumerate(line):
                if ch == cross:
                    if check_axis(axis1_dirs) and check_axis(axis2_dirs):
                        total += 1
        print(total)

def main():
    path = Path(__file__).parent
    ws = WordSearch(path / "search.txt")
    # ws.print_wordsearch()
    word = 'XMAS'
    ws.find(word)
    word = 'MAS'
    ws.x_find(word)

if __name__ == '__main__':
    main()
    
