def words_length_dict(sentence):
    words = sentence.split()
    return {word: len(word) for word in words}

sentence = "Привет мир это тест"
length_dict = words_length_dict(sentence)
print("Словарь слов и их длины:", length_dict)
