from fastapi import FastAPI

app = FastAPI()

#path parameter 

@app.get("/display/{id}")
def view(id:int):
    return id
    pass
        cd