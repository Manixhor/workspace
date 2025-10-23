string = "ndjfk"

rever = ""
#for i in range(len(string)-1,-1,-1):
#	rever = rever + string[i]
#	
#if string == rever:
#	print("palin")
#	
#	

for i in string:
	if i not in rever:
		rever = i + rever
if string == rever:
	print("yep")