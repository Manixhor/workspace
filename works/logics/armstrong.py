num = int(input("enter your number"))


string_num = str(num)
length_num = len(string_num)

sum = 0 
for digit in string_num:
    sum += int(digit) ** length_num

if sum == num:
    print("It is a armstrong number")
else:
    print("It is not a armstrong number")