import re
from pathlib import Path

class MulFix:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.get_data()

    def get_data(self):
        data = str()
        with open(self.filename, 'r') as file:
            data = file.read()
        return data

    def get_muls(self):
        total = 0
        pairs = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", self.data)
        nums = [tuple(map(int,pair)) for pair in pairs]
        for x,y in nums:
            total += x * y
        print(f'Total of mul operations = {total}')

    def get_muls_with_do_donts(self):
        total = 0
        enabled = True
        pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
        matches = re.finditer(pattern, self.data)
        for m in matches:
            token = m.group(0)
            if token == "do()":
                enabled = True
            elif token == "don't()":
                enabled = False
            elif token.startswith("mul"):
                if enabled:
                    nums = re.findall(r"(\d{1,3}),(\d{1,3})", token)
                    x,y = map(int, nums[0])
                    total += x * y
        print(f'Total = {total}')


def main():
    path = Path(__file__).parent
    mf = MulFix(path / "memory.txt")
    # mf.get_muls()
    mf.get_muls_with_do_donts()
    
if __name__ == '__main__':
    main()
