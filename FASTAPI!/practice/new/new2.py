from fastapi import FastAPI,Query
emp = [

    {'id': 101,'name':'CSE',"place":"cjsd"},
    {'id': 102,'name':"mani","place":"cnkcd"},
    
]
app = FastAPI()

@app.get("/display/{name}")

def view(name:str):
    for e in emp:
        if e['name'] == name:
            return e 


# @app.get("/display")
# #no need to mention "?" for this 
# def viewforquery(id:int = Query(ge=100,le=200)):
#     for e in emp:
#         if e['id'] == id:
#             return e 
        
@app.get("/display")
#no need to mention "?" for this 
def viewforquery(id:int=Query(ge=100,le=200),name:str=Query(min_length=3,max_length=20,regex="^[A-Z,a-z]")):

    for e in emp:
        if e['id'] == id and e['name'].lower() == name.lower():
            return e 
        
