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

    def find(self, word):
        print(f'Finding {word}...')
        total = 0
        for row, line in enumerate(self.data):
            for col, ch in enumerate(line):
                if self.data[row][col] == word[0]:
                    for dr, dc in self.directions:
                        if 0 <= row + dr * (len(word)-1) < len(self.data) and \
                        0 <= col + dc * (len(word)-1) < len(self.data[0]):
                            match = True
                            for i in range(1, len(word)):
                                if self.data[row + dr * i][col + dc * i] != word[i]:
                                    match = False
                                    break
                            if match:
                                total += 1
        print(f'Total found = {total}')

    def x_find(self, word):
        total = 0
        n = len(word)
        cross = word[n//2]
        for row, line in enumerate(self.data):
            for col, ch in enumerate(line):
                if self.data[row][col] == cross:
                    pass


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
    
