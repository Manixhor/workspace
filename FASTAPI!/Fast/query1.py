from fastapi import FastAPI,Query,Path
emp = [

    {'id': 101,'name':'CSE',"place":"cjsd"},
    {'id': 102,'name':"mani","place":"cnkcd"},
    
]
app = FastAPI()


@app.get("/display/query")
#no need to mention "?" for this 
def viewforquery(name:str):
    for e in emp:
        if e['name'] == name:
            return e 