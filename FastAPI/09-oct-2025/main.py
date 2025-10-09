from fastapi import FastAPI 

app = FastAPI()
@app.get("/home_page")

def hello():
	return {"Hello world"}
	
@app.get("/doc")
def docsu():
	return {"docs":"http://127.0.0.1:8000/docs"}