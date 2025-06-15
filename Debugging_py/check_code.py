# Исходный список
original_list = ["aa", "--", "wR", "--", "--", "aa", "aa", "--"]

# Находим индекс первого вхождения "aa"
try:
    first_index = original_list.index("aa")
except ValueError:
    first_index = None  # Если "aa" нет в списке

# Находим индекс второго вхождения "aa"
try:
    second_index = original_list.index("aa", first_index + 1)
except ValueError:
    second_index = None  # Если второго "aa" нет в списке

# Выводим результаты
print(f"Индекс первого 'aa': {first_index}")
print(f"Индекс второго 'aa': {second_index}")
