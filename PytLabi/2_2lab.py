def find_min_index(numbers):
    if not numbers:  # Проверка на пустой список
        return None
    min_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[min_index]:
            min_index = i
    return min_index

numbers_list = [3, 1, 4, 1, 5, 9, 2]
min_index = find_min_index(numbers_list)
print("Индекс минимального элемента:", min_index)
