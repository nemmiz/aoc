foods = []
with open('../input/21.txt') as stream:
    for line in stream:
        ingredients, allergens = line.split(' (contains ')
        ingredients = set(ingredients.split())
        allergens = set(allergens.strip().replace(',', '').replace(')', '').split())
        foods.append((ingredients, allergens))

ingredients = set()
for i, _ in foods:
    ingredients.update(i)

ingredients_with_allergens = {}
ingredients_without_allergens = set()
for ingredient in ingredients:
    potential_allergens = set()
    for i, a in foods:
        if ingredient in i:
            potential_allergens.update(a)
    does_not_contain = set()
    for mc in potential_allergens:
        for i, a in foods:
            if mc in a and ingredient not in i:
                does_not_contain.add(mc)
    potential_allergens = potential_allergens.difference(does_not_contain)
    if potential_allergens:
        ingredients_with_allergens[ingredient] = potential_allergens
    else:
        ingredients_without_allergens.add(ingredient)

n = 0
for i, _ in foods:
    for ing in i:
        if ing in ingredients_without_allergens:
            n += 1
print(n)

allergens = {}
while len(allergens) != len(ingredients_with_allergens):
    for i, potential_allergens in ingredients_with_allergens.items():
        known_allergens = set(allergens.keys())
        potential_allergens = potential_allergens.difference(known_allergens)
        if len(potential_allergens) == 1:
            allergen = next(iter(potential_allergens))
            allergens[allergen] = i

tmp = [(a, i) for a, i in allergens.items()]
tmp.sort()
print(','.join(i for _, i in tmp))
