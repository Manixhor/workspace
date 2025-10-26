text=input()
def rev():
    result = ""
    for txt in text:
        if txt not in result:
            result = txt + result
    return result

print(rev())  

