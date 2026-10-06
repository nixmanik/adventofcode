from functools import cmp_to_key

class PrintQueue:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            raw_data = f.read().strip()
        raw_rules, raw_pagesets = raw_data.split('\n\n')
        self.rules = set()
        for line in raw_rules.splitlines():
            x,y = map(int, line.split('|'))
            self.rules.add((x,y))
        self.pagesets = []
        for line in raw_pagesets.splitlines():
            pages = list(map(int, line.split(',')))
            self.pagesets.append(pages)

    def is_pageset_valid(self, pageset) -> bool:
        seen = set()
        for page in pageset:
            for seen_page in seen:
                if (page, seen_page) in self.rules:
                    return False
            seen.add(page)
        return True

    def sort_pageset(self, pageset) -> list:
        def compare_pages(x,y):
            if (x,y) in self.rules:
                return -1
            if (y,x) in self.rules:
                return 1
            return 0
        return sorted(pageset, key=cmp_to_key(compare_pages))

    def get_midpoint_value(self, pageset) -> int:
        mid = len(pageset) // 2
        return pageset[mid]

    
def main():
    pq = PrintQueue('data.txt')
    total = 0
    total_fixed = 0
    for ps in pq.pagesets:
        if pq.is_pageset_valid(ps):
            print(f'Valid: {ps}')
            total += pq.get_midpoint_value(ps)
        else:
            fixed_ps = pq.sort_pageset(ps)
            print(f'Invalid fixed: {fixed_ps}')
            total_fixed += pq.get_midpoint_value(fixed_ps)


    print(total)
    print(total_fixed)





if __name__ == '__main__':
    main()
