from fastapi import FastAPI,Query,Path
emp = [

    {'id': 101,'name':'CSE',"place":"cjsd"},
    {'id': 102,'name':"mani","place":"cnkcd"},
    
]
app = FastAPI()

@app.get("/display/{id}")

@app.get("/display")
#no need to mention "?" for this 
def viewforquery(id:int = Query(ge=100,le=200)):
    for e in emp:
        if e['id'] == id:
            return e 