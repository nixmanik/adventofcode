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

        for ch in self.data[0]:
            if ch == term[0]:
                print('found')

def main():
    path = Path(__file__).parent
    ws = WordSearch(path / "search.txt")
    # ws.print_wordsearch()
    term = 'XMAS'
    ws.find(term)

if __name__ == '__main__':
    main()
    
