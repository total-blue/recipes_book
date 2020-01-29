file = open('recipes.txt')
keys = ['ingredient_name', 'quantity', 'measure']
cook_book = {}
ings = []

while True:
    dish_name = file.readline().strip()
    ret = file.readline()
    for i in range(int(ret)):
        ing = dict(zip(keys,(file.readline().strip().split(' | '))))
        ing['quantity'] = int(ing['quantity'])
        ings.append(ing)
    if not file.readline(): break
    cook_book[dish_name] = ings
    ings = []

def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    for dish in set(dishes):
        if not dish in cook_book:
            print(f'no dish named {dish}')
        else:
            mult = dishes.count(dish)
            dish_ings = cook_book.get(dish)
            for ing in dish_ings:
                ing['quantity'] = int(ing['quantity']) * person_count * mult
                shop_dict[ing.pop('ingredient_name')] = ing
            print(shop_dict)
