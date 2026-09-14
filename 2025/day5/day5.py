def get_data():
    fresh_ids = []
    ingredient_ids = []
    fresh_ids_complete = False

    with open('ingredients.txt', 'r') as file:
        for line in file:
            line = line.strip()

            if not line:
                fresh_ids_complete = True
                continue

            if not fresh_ids_complete:
                start, end = line.split('-')
                for num in range(int(start), int(end) + 1):
                    fresh_ids.append(num)
                
            else:
                ingredient_ids.append(int(line))

    return fresh_ids, ingredient_ids

def available_fresh(fresh_ids, ing_ids):
    available = []
    for ing in ing_ids:
        if ing in fresh_ids:
            available.append(ing)
    return available

def main():
    fresh, ing = get_data()
    available = available_fresh(fresh, ing)
    print(len(available))

if __name__ == "__main__":
    main()