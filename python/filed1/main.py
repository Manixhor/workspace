from fastapi import FastAPI 
"""path parameter"""
#creating a object 
result = [
{"name":"CSE","id":101,"place":"Hyderabad"},{"name":"Mani","id":102,"place":"Pune"}] #this is a JSON format 
app = FastAPI()
#that {} called the path parameter
@app.get("/display/{place}")
def writingpath(place:str): #here we are making sure that id should be in crct format
	for res in result:
		if res['place'] ==place:
			return res
@app.get("/display")
def viewforquery(id : int):
	for q in result:
		if q['id'] == id:
			return q

	
	
	