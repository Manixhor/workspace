num = 1234
num_string = str(num)

for n in num_string:
    if n not in result:
        result = num_string + result

print(result)