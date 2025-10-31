text = "mannni"

freq = {}

def fre1q():
    for i in text:
        if i in freq:
            freq[i] += 1 
        else:
            freq[i] = 1
    return freq

print(fre1q())