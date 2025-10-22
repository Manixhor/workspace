string = "word"

result = ""
#we can't append the string only list can do that
for i in string:
    if i not in result:
        result = i + result

print(result)