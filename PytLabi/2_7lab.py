def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

string1 = "listen"
string2 = "silent"
print(f"'{string1}' и '{string2}' являются анаграммами: {are_anagrams(string1, string2)}")
