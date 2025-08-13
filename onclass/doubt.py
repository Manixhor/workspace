
def is_leap(year):
    leap = year%4
    if leap == 0:
        print(True)
    else:
        print("False")
    #leap = False
    
    
    # Write your logic here
    

year = int(input())
print(is_leap(year))