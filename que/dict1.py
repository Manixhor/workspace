#merging two dict 

dict12 = {"Name":"Mani","age": 23}
dict2 = {"clg":"VIT","year": 2025}

dict3 = dict12 | dict2 
dict4 = {**dict12,**dict2}

print(dict3)
print(dict4)