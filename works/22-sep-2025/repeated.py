numbers = [1, 2, 2, 3, 3, 3, 4]

checked = []   

for num in numbers:
    if num not in checked:        
        count = 0
        for other in numbers:    
            if num == other:
                count = count + 1
        print(num, "comes", count, "times")
        checked.append(num)      
