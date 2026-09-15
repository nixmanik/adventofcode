def get_data():
    fresh_ids = []
    ingredient_ids = []
    fresh_ids_complete = False

    with open('ingredients.txt', 'r') as file:
        for line in file:
            l = line.strip()
        
            if not l:
               print("line break")
               continue

            if '-' in l:
                print(f'Fresh ID range: {l}')
                start, end = l.split('-')
                fresh_ids.append((int(start), int(end)))
            elif l.isalnum():

                # print(f'Ingredient ID: {line}')
                ingredient_ids.append(int(l))

    return fresh_ids, ingredient_ids

def available_fresh(fresh_ids, ing_ids):
    available = []
    for ing in set(ing_ids):
        for start,end in fresh_ids:
            if start <= ing <= end:
                available.append(ing)
                break
    return available

def all_fresh_count(fresh_ids):
    fresh_ids.sort(key=lambda x: x[0])
    # print(fresh_ids)
    merged = [fresh_ids[0]] if fresh_ids else []
    for current in fresh_ids[1:]:
        prev_s, prev_e = merged[-1]
        curr_s, curr_e = current

        if curr_s <= prev_e + 1:
            merged[-1] = prev_s, max(prev_e, curr_e)
        else:
            merged.append(current)
    return sum(end - start + 1 for start, end in merged)


def main():
    fresh, ing = get_data()
    available = available_fresh(fresh, ing)
    print(len(available))
    print(all_fresh_count(fresh))

if __name__ == "__main__":
    main()