from fastapi import FastAPI

app = FastAPI()

@app.get("/intro")
def read_root():
    return {"Hey this is mani welcome to FASTAPI Learnings."}
