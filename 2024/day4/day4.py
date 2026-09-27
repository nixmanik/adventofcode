from pathlib import Path

class WordSearch:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        with open(filename, 'r') as file:
            self.data = [list(line.strip()) for line in file]

    def print_wordsearch(self):
        for line in self.data:
            print(line)

    def find(self, term):
        total = 0
        directions = [
                (0,1),(0,-1),(1,0),(-1,0),
                (1,1),(-1,-1),(-1,1),(1,-1)
        ]
        for row, line in enumerate(self.data):
            for col, ch in enumerate(line):
                if self.data[row][col] == term[0]:
                    for dr, dc in directions:
                        if 0 <= row + dr * (len(term)-1) < len(self.data) and \
                        0 <= col + dc * (len(term)-1) < len(self.data[0]):
                            match = True
                            for i in range(1, len(term)):
                                if self.data[row + dr * i][col + dc * i] != term[i]:
                                    match = False
                                    break
                            if match:
                                total += 1
        print(f'Total found = {total}')




def main():
    path = Path(__file__).parent
    ws = WordSearch(path / "search.txt")
    # ws.print_wordsearch()
    term = 'XMAS'
    ws.find(term)

if __name__ == '__main__':
    main()
    
