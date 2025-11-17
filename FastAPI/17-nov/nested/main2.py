from fastapi import FastAPI

app = FastAPI()

@app.get("/display/{item:id}")
def view(id:int):
    return f"{id}"

