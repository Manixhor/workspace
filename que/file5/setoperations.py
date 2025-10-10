def  set_operations(list1,list2):
	set1,set2 = set(list1),set(list2)
	
	return {
		"union": list(set1 | set2),
		"intersection": list(set1 & set2),
		"difference" : list(set1-set2)
		
	}
	
print(set_operations([1,5,6,4],[2,3,4,5,6]))