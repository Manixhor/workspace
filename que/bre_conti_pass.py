#it breaks the loop and discontinue the code
for i in range(5):
    if i == 2:
        break
    print(i)
#here it skips 2 value and continues the loop
for i in range(5):
    if i == 2:
        continue
    print(i)
#here it does nothing 
"""the purpose of pass if there is an empty cls or function
the code get's error so to avoid that pass is used """
for i in range(5):
    if i == 2:
        pass
    print(i)

    
    