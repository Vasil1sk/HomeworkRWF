with open("recipes.txt", "rt", encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        dish_quantity = int(file.readline())
        ingredients = []
        for ingredient in range(dish_quantity):
            ingr = file.readline().strip()
            ingredient_name, quantity, measure = ingr.split(" | ")
            ingredients.append({
                "ingredient_name": ingredient_name,
                "quantity": quantity,
                "measure": measure
            })
        file.readline()
        cook_book[dish_name] = ingredients

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingrs in cook_book.get(dish):
                shop_list[ingrs["ingredient_name"]] = {"measure": ingrs["measure"], "quantity": int(ingrs["quantity"]) * int(person_count)}
    return shop_list

name_len = {}
name_text = {}

with open("1.txt", "rt", encoding="utf-8") as file1:
    file1_name = "1.txt"
    len_lines = 0
    lines_of_text = []
    for line in file1:
        len_lines += 1
        lines_of_text.append(line)
        name_text[file1_name] = lines_of_text
    name_len[file1_name] = len_lines

with open("2.txt", "rt", encoding="utf-8") as file2:
    file2_name = "2.txt"
    len_lines = 0
    lines_of_text = []
    for line in file2:
        len_lines += 1
        lines_of_text.append(line)
        name_text[file2_name] = lines_of_text
    name_len[file2_name] = len_lines

with open("3.txt", "rt", encoding="utf-8") as file3:
    file3_name = "3.txt"
    len_lines = 0
    lines_of_text = []
    for line in file3:
        len_lines += 1
        lines_of_text.append(line)
        name_text[file3_name] = lines_of_text
    name_len[file3_name] = len_lines

sorted_dict = dict(sorted(name_len.items(), key=lambda item: item[1]))

with open("Sorted texts.txt", "wt", encoding="utf=8") as new_file:
    for key, value in sorted_dict.items():
        new_file.writelines("\n" + key + "\n")
        new_file.writelines(str(value) + "\n")
        for new_line in name_text[key]:
            new_file.writelines(new_line)


print(get_shop_list_by_dishes(["Омлет", "Утка по-пекински"], 2))