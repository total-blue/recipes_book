#1
with open('recipes.txt') as f:
    cook_book = {}
    keys = ('ingredient_name', 'quantity', 'measure')
    i = iter(f)
    try:
        while True:
            name, amount = next(i).rstrip(), next(i)
            cook_book[name] = []
            for line in range(int(amount)):
                cook_book[name].append(dict(zip(keys, (next(i).rstrip().split('|')))))
            next(i)
    except StopIteration:
        pass

#2
with open('recipes.txt') as f:
    def get_shop_list_by_dish(dishes, person_count):
        cook_book = f.read().split('\n')
        keys = ['quantity', 'measure']
        rec_dict = {}
        dish_inds = []
        for dish in dishes:
            for line in cook_book:
                if line == dish:
                    dish_inds.append(cook_book.index(line))
        for dish_ind in dish_inds:
            ret = int(cook_book[dish_ind+1])
            ing_list = cook_book[dish_ind+2:dish_ind+2+ret]
            for ing in ing_list:
                x = ing.split('|')
                rec_dict[x[0]] = dict(zip(keys, (int(x[1]) * person_count, x[2])))
        if not rec_dict == {}:
            print(rec_dict)
        else:
            print('There are no your dishes')
