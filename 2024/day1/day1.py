from collections import Counter
def get_data(filename):
    lista, listb = [], []
    with open(filename, 'r') as file:
        for line in file:
            a,b = line.strip().split()
            lista.append(int(a))
            listb.append(int(b))
    lista.sort()
    listb.sort()
    return lista, listb

def get_diffs(a, b): 
    diffs = []
    for x,y in zip(a,b):
        diffs.append(abs(x-y))
    return sum(diffs)

def get_sim_score(a, b):
    seenb = Counter(b)
    score = [num * seenb[num] for num in a]
    return sum(score)

def print_solution(diffs, simscore):
    print(diffs)
    print(simscore)

def main():
    filename = 'day1.txt'
    a, b = get_data(filename)
    diffs = get_diffs(a,b)
    score = get_sim_score(a,b)
    print_solution(diffs,score)

if __name__ == '__main__':
    main()
