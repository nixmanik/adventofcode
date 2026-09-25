class MultFixer:
    def __init__(self,filename):
        self.filename = filename
        self.data = self.get_data()

    def get_data(self):
        data = []
        with open(self.filename, 'r') as file:
            for line in file:
                for ch in line:
                    data.append(ch)
        return data

    def find_mults(self):
        stack = []
        total = 0
        for i in range(len(self.data)):
            check = ''.join(self.data[i:i+3])
            print(check)
            if check == 'mul':



def main():
    mf = MultFixer('memory.txt')
    mf.find_mults()

if __name__ == '__main__':
    main()

