#import csv file
import csv
import os
import re
# import the csv file

def standardize_unit(units):
    unit_mapping = {

    }
    return unit_mapping.get(units, units)

all_dishes = []
for f in os.listdir('./data/dishes'):
    if f.endswith('.csv'):
        with open(f'./data/dishes/{f}', 'r', encoding='utf-8') as file:
            reader = csv.reader(file )
            dishes = [row for row in reader][1:]
            for dish in dishes:
                all_dishes.append(dish)


all_ingredients = []
for name, recipe, tags in all_dishes[1:2]:
    print(name) 
    for step in recipe.split('<br>'):
        print(step)
    print(tags) 
    for steps in recipe.split('<br>'):
        amounts = re.findall(r'<i>(.*?)</i>', steps)
        ingridents = re.findall(r'<b>(.*?)</b>', steps)
        for i, ingredient in enumerate(ingridents):
            amount, unit = amounts[i].split(' ', 1) if i < len(amounts) else (0, '')
            unit = standardize_unit(unit)
            all_ingredients.append((ingredient, amount, unit))


    