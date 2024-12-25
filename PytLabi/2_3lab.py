def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Пример использования
input_string = "hello world"
character_counts = count_characters(input_string)
print("Количество символов в строке:", character_counts)
