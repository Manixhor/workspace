
string1 = "hello"

char_dict = {}
for i in string1:
    if i in char_dict:
        char_dict[i] = char_dict[i] + 1
    else:
        char_dict[i] = 1

print(char_dict)