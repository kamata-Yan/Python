def remove_above_average(numbers):
    average = sum(numbers) / len(numbers)
    return [num for num in numbers if num <= average]

numbers_list = [10, 20, 30, 40, 50]
filtered_numbers = remove_above_average(numbers_list)
print("Список после удаления элементов выше среднего:", filtered_numbers)
