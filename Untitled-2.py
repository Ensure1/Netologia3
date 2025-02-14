cook_book = {
    "Омлет": [
        {"ingredient_name": "Яйцо", "quantity": 2, "measure": "шт"},
        {"ingredient_name": "Молоко", "quantity": 100, "measure": "мл"},
        {"ingredient_name": "Помидор", "quantity": 2, "measure": "шт"}
    ],
    "Утка по-пекински": [
        {"ingredient_name": "Утка", "quantity": 1, "measure": "шт"},
        {"ingredient_name": "Вода", "quantity": 2, "measure": "л"},
        {"ingredient_name": "Мед", "quantity": 3, "measure": "ст.л"},
        {"ingredient_name": "Соевый соус", "quantity": 60, "measure": "мл"}
    ],
    "Запеченный картофель": [
        {"ingredient_name": "Картофель", "quantity": 1, "measure": "кг"},
        {"ingredient_name": "Чеснок", "quantity": 3, "measure": "зуб"},
        {"ingredient_name": "Сыр гауда", "quantity": 100, "measure": "г"}
    ]
}

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient["ingredient_name"]
                quantity = ingredient["quantity"] * person_count
                measure = ingredient["measure"]
                if name in shop_list:
                    shop_list[name]["quantity"] += quantity
                else:
                    shop_list[name] = {"measure": measure, "quantity": quantity}
    return shop_list

# Пример вызова функции
print(get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2))

import os

def merge_files(file_list, output_file):
    file_data = []
    
    # Читаем содержимое файлов и сохраняем их с информацией о количестве строк
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            file_data.append((file, len(lines), lines))
    
    # Сортируем файлы по количеству строк
    file_data.sort(key=lambda x: x[1])
    
    # Записываем в итоговый файл
    with open(output_file, 'w', encoding='utf-8') as out:
        for file_name, line_count, lines in file_data:
            out.write(f"{file_name}\n")
            out.write(f"{line_count}\n")
            out.writelines(lines)
            out.write("\n")

# Пример использования
file_list = ["1.txt", "2.txt"]  # Укажите реальные файлы
output_file = "result.txt"
merge_files(file_list, output_file)